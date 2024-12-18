.. currentmodule:: howso.engine

Trainee Persistence
===================
.. topic:: What is covered in this user guide.

    In this guide, you will learn the options available to control when a trainee's state is saved to disk.

Prerequisites: before you begin
-------------------------------
- **Installation** - You have successfully installed :doc:`Howso Engine <../../getting_started/installing>`.
- You have an understanding of  :doc:`loading and saving trainees <../basic_capabilities/save_load_delete>`.

Concepts & Terminology
----------------------
A :py:class:`howso.engine.Trainee` object can be created with a ``persistence`` setting.  Allowed values are:

``never``
    A trainee only exists in memory; :py:meth:`Trainee.persist()` is an error.

``allow`` (default)
    A trainee principally exists in memory, but :py:meth:`Trainee.persist()` will write it to disk.

``always``
    A trainee principally exists in memory, but its contents are automatically written to disk after each operation.

A trainee created with ``persistence='always'`` can also be set to *transactional mode*, where changes are appended to the on-disk file, rather than writing a new file every time a call is made.  This generally results in faster operation, but the incremental data can become large, and manual :py:meth:`Trainee.persist()` calls are necessary to reduce the data size.

How-To Guide
------------

These instructions apply to the :py:class:`howso.direct.HowsoDirectClient` from the ``howso-engine`` Python package.  Other client implementations may have different interpretations of these settings.

Persisting
^^^^^^^^^^

The :py:meth:`Trainee.persist()` call will write the trainee to disk.  This creates a snapshot of the current trainee's state.  By default, the file is stored in the current directory with the trainee's unique identifier as a filename.

.. code-block:: python

    from pathlib import Path

    trainee.persist()
    trainee_path = Path.cwd() / f"{trainee.id}.caml"
    assert trainee_path.exists()

The persisted file is in the same format as a file written by :py:meth:`Trainee.save()`, but the Howso Engine library chooses the file path.  This means, if you know the persisted trainee's file path, you can :py:func:`load_trainee()` the saved trainee.  Note that the loaded trainee will be assigned a new unique ID.

.. code-block:: python

    saved_trainee_file = Path("saved-trainee.txt")
    if saved_trainee_file.exists():
        trainee = load_trainee(saved_trainee_file.read_text())
    else:
        trainee = Trainee()
    saved_trainee_file.write_text(f"{trainee.id}.caml")

Calling :py:meth:`Trainee.delete()` will delete the persisted file.  You can copy the persisted trainee somewhere else, or explicitly :py:meth:`Trainee.save()` to write its data somewhere else.

Persistence Modes
^^^^^^^^^^^^^^^^^

A :py:class:`Trainee` object can be created with a ``persistence`` setting.  This controls whether :py:meth:`Trainee.persist()` can be called, and it can cause it to be called automatically if needed.

If a Trainee is created with ``persistence='never'`` then it cannot be persisted.  The :py:meth:`Trainee.persist()` call will result in an exception.  This is an instruction to the client library that the trainee state needs to be kept only in memory, independent of any particular client library implementation.

The default setting for a Trainee is ``persistence='allow'``.  The client in the *howso-engine* Python package interprets this to mean that data will only be written when :py:meth:`Trainee.persist()` is explicitly called.

``persistence='always'`` causes the library to call :py:meth:`Trainee.persist()` itself after every operation.  In this mode, application code does not need to call :py:meth:`Trainee.persist()` itself.

For example:

.. code-block:: python

    trainee1 = Trainee(persistence='never')
    trainee1.train(df)
    # trainee1.persist()  # would throw an exception

    trainee2 = Trainee(persistence='allow')
    trainee2.train(df)
    trainee2.persist()    # writes {trainee2.id}.caml

    trainee3 = Trainee(persistence='always')
    trainee3.train(df)    # writes {trainee3.id}.caml
    # trainee3.persist()  # would rewrite the same file

Similar persistence settings exist on :py:func:`load_trainee()` and :py:meth:`Trainee.copy()`.  Each copy of a trainee has its own persistence setting.  It is possible to implicitly write a trainee in always-persist mode, and load that on-disk state into a never-persist in-memory trainee.

Transactional Mode
^^^^^^^^^^^^^^^^^^

.. versionadded:: 33.1

If a trainee is created with ``persistence='always'``, it can also be created in *transactional mode*.  In this mode, every operation appends a change to the on-disk trainee file.  The file must be reloaded in transactional mode as well.  This generally results in faster execution, since only the changes from the most recent operation need to be written, but the resulting on-disk file may be substantially larger.

Transactional mode is a client-specific option, and can be enabled using a ``runtime`` setting:

.. code-block:: python

    trainee = Trainee(persistence='always', runtime={'transactional': True})

This works in the same way as the always-persist mode shown above: data is implicitly written after each operation, without intervention from code.

.. code-block:: python

    trainee4 = Trainee(persistence='always', runtime={'transactional': True})
    trainee4.train(df)

    trainee5 = load_trainee(f"{trainee4.id}.caml",
                            persistence='always', runtime={'transactional': True})
    trainee5.get_num_training_cases()  # includes the total from the `train()` call

When there are small updates to an otherwise large trainee file, transactional mode can be substantially faster.  If a trainee has 1 million cases in it and a :py:meth:`Trainee.train()` call adds 100 more, transactional mode will only append the new cases to the file, rather than rewriting the entire trainee state.

If there are significant updates to an otherwise small trainee file, transactional mode can result in a substantially larger file size.  If code relies on automatic persistence, workloads with many ``train()`` calls or other small data updates can result in a file size 10x or more larger than a non-transactional file.

In transactional mode, an explicit call to :py:meth:`Trainee.persist()` will compact the file and discard the transaction log.

As a simple example, consider removing a feature definition from the trainee metadata.  This would typically make the trainee state size smaller.  In transactional mode, though, this would be recorded as an additional change appended to the file, and the resulting file will be larger.  Calling :py:meth:`Trainee.persist()` will compact the file, discarding the original feature definition.

.. code-block:: python

    # Create the trainee
    trainee = Trainee(features={"one": {"type": "nominal"}, "two": {"type": "nominal"},
                      persistence='always', runtime={'transactional': True})

    # Examine the file size
    trainee_path = tmp_path / f"{trainee.id}.caml"
    old_size = trainee_path.stat().st_size

    # Discard the second feature
    trainee.set_feature_attributes({"one": {"type": "nominal"}})
    new_size = trainee_path.stat().st_size  # will be larger than old_size

    # Compact the file
    trainee.persist()
    compacted_size = trainee_path.stat().st_size  # will be smaller than old_size

Transactional mode is intended for trainees with small, frequent updates.  Code needs to make sure to periodically call :py:meth:`Trainee.persist()` to limit the file size.  A simple setup would call ``persist()`` once for about every 10 calls to other :py:class:`Trainee` methods that change the trainee state, getting most of the performance benefit of transactional mode while generally limiting the file size.
