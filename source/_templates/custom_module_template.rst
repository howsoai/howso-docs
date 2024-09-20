{{ fullname | escape | underline }}

.. currentmodule:: {{ fullname }}

{% block modules %}
{% if modules %}
.. rubric:: Submodules

.. autosummary::
   :toctree:
   :template: custom_module_template.rst
   :recursive:
{% for item in modules %}
{% if 'test' not in item %}
   {{ item }}
{%- endif %}
{%- endfor %}
{%- endif %}
{% endblock %}

{% block classes %}
{% if classes %}
.. rubric:: Classes

.. autosummary::
   :nosignatures:
{% for item in classes %}
   ~{{ fullname }}.{{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

{% block functions %}
{% if functions %}
.. rubric:: Functions

.. autosummary::
   :nosignatures:
{% for item in functions %}
   ~{{ fullname }}.{{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

{% block attributes %}
{% if attributes %}
.. rubric:: Attributes

.. autosummary::
   :nosignatures:
{% for item in attributes %}
   ~{{ fullname }}.{{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

.. automodule:: {{ fullname }}
   :members:
   :no-undoc-members:
   :show-inheritance:
