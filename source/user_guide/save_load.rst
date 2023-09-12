.. currentmodule:: howso.engine

Saving and Loading
==================
.. topic:: What is covered in this user guide.

   In this guide, you will learn how to save and load :py:class:`~Trainee` s using the built-in Howso Engine's file operations.

Objectives: what you will take away
-----------------------------------
- **Definitions & Understanding** of different saving and loading operations based on platform.
- **How-To** Save and load a :py:class:`~Trainee`.
- **API References** How to use, :meth:`Trainee.save`, :py:meth:`Engine.load_trainee`, :py:meth:`Trainee.persist`, and :py:meth:`Trainee.acquire_resources`.

Prerequisites
-------------
- You have successfully :doc:`installed Howso Engine <../getting_started/installing>`
- You have :doc:`loaded, configured, trained, and analyzed data <basic_workflow>`

Notebook Recipe
---------------
The following recipe will supplement the content this guide will cover:

- :download:`Engine Intro <https://github.com/howsoai/howso-engine-recipes/blob/main/1-engine-intro.ipynb>`

Concepts & Terminology
----------------------
The main concept of this guide is how to save and load a Trainee. To understand this better, we
recommend being familiar with the Trainees:

- :ref:`Trainee <user_guide/terminology:trainee>`

How-To Guide
------------

Methods for Saving and Loading
------------------------------

Howso Engine can be operated locally or through the Howso Platform as part of an enterprise License. In order to accommodate both sets configurations, the Trainee has two sets of
saving and loading functions that is intended for different types of operations.

- **File Operations** - A set of functions that allows a user to save and load to a specific file location. Trainees are saved as ``.caml`` files, which stands for Compressed `Amalgam <https://github.com/howsoai/amalgam/>`__. This is the method that will most likely be used by non enterprise users.

- **Database Operations** The database set of operations provides better integration with databases and the Howso Platform. These methods abstract away some of the specifics of saving and loading and allows users to refer to Trainees by name only. Database operations revolves around the terminology, ``persist`` and ``acquire resources``, as opposed to save and load to better reflect the nature of what is occuring.


File Operations
---------------


Saving
^^^^^^
Saving Trainees to your local file system can be done using the :meth:`Trainee.save` function. The  :meth:`Trainee.save` function has one optional parameter, ``filename``, which lets the user specify where to save the file and what to name the saved file. The ``filename`` parameter can consist of:

- **Absolute path** A file path may be an absolute path, optionally with a Trainee filename ending with ``.caml``.

- **Relative path** A file path may also be a relative path to the current working directory, optionally with a Trainee filename ending with ``.caml``.

- **File name only** Just the trainee filename may be provided, in which case the Trainee will be saved to the default location which is the current working directory.

- **None** If the ``filename`` parameter is not used, then the Trainee will be saved to the default location using the Trainee ID.

.. code-block:: python
    :caption: Saving Example:

    # Create a Trainee Object.
    t = Trainee()

    # Train Trainee on the data.
    t.train(df)

    # Save the Trainee
    t.save(filepath='example_location/example_trainee.caml')

Loading
^^^^^^^

The  :meth:`Engine.load_trainee` function has one parameter, ``filename``, which lets the user specify where to load the file. The ``filename`` parameter can consist of either:

- **Absolute path** A file path may be an absolute path with a Trainee filename ending with ``.caml``.

- **Relative path** A file path may also be a relative path to the current working directory, with a Trainee filename ending with ``.caml``.

- **File name only** Just the trainee filename may be provided, in which case the Trainee will be retrieved from the default location which is the current working directory.

.. code-block:: python
    :caption: Loading Example:

    # Import the `load_trainee` function
    from howso.engine import load_trainee

    # Load the trainee
    t = load_trainee(file_path='example_location/example_trainee.caml')


Database Operations
--------------------

As explained earlier, database operations is designed to be used with the Howso Platform, a cloud based service for enterprise users. In this set of operations,
:py:meth:`Trainee.persist` saves the trainee while :py:meth:`Trainee.acquire_resources` then loads the trainee resources back. All of this can be handled using the same Trainee, with the Trainee name used as the identifier behind the scenes to save and load.

.. code-block:: python
    :caption: Saving and Loading using Database Operations Example:

    with engine.Trainee(name=trainee_name, features=features) as t:
        # Save the trainee.
        t.persist()

        # Release the trainee resources.
        t.release_resources()

        # Acquire new trainee resources. (Optional, this will happen automatically if the trainee is unavailable.)
        t.acquire_resources()

        # Delete the trainee to cleanup.
        t.delete()

These methods can be used locally as well, but you do not have control over the exact naming and location of the saved Trainee. File operations are recommended when loading and saving to disk.