import os
from typing import Any, Dict

from howso.client.api import get_api
from jinja2 import BaseLoader, Environment
from jinja2.exceptions import UndefinedError
from sphinx.util import logging

logger = logging.getLogger(__name__)


def setup(app):
    """
    Setup function for the Sphinx extension.
    This builds RST pages for the needed Engine type schemas.
    """
    def generate_rst_from_json(app):
        """
        Function that runs before Sphinx starts reading source files.
        Place your JSON fetching and RST generation code here.
        """
        try:
            needed_schemas = [
                "FeatureAttributes",
                "FeatureAutoDeriveOnTrain",
                "FeatureBounds",
                "FeatureDataType",
                "FeatureOriginalType",
                "FeatureOriginalTypeBoolean",
                "FeatureOriginalTypeContainer",
                "FeatureOriginalTypeDate",
                "FeatureOriginalTypeDatetime",
                "FeatureOriginalTypeInteger",
                "FeatureOriginalTypeNumeric",
                "FeatureOriginalTypeObject",
                "FeatureOriginalTypeString",
                "FeatureOriginalTypeTime",
                "FeatureOriginalTypeTimedelta",
                "FeatureOriginalTypeTokenizableString",
                "FeatureTimeSeries",
                "FeatureType",
            ]

            # THIS WILL NOT WORK IF HOWSO-ENGINE-PY IS INSTALLED EDITABLY
            # (unless you have the .caml in your local repo too)
            schema_map = get_api()['schemas']
            os.makedirs(
                os.path.join(app.srcdir, 'howso', 'types'),
                exist_ok=True
            )
            for schema_name in needed_schemas:
                schema = schema_map[schema_name]
                if schema is None:
                    print(schema_name)
                    continue
                try:
                    rst_output = generate_sphinx_doc(schema, schema_name)
                except UndefinedError as e:
                    print(schema_name)
                    print(schema)
                    print(e)
                    continue
                with open(
                    os.path.join(
                        app.srcdir,
                        'howso',
                        'types',
                        f'{schema_name}.rst'
                    ),
                    'w'
                ) as f:
                    f.write(rst_output)

            logger.info((
                'Successfully generated Howso Engine Feature Attributes '
                'RST files from JSON data'
            ))
        except Exception as e:
            logger.error(f'Error generating RST files: {str(e)}')
            raise

    # Connect to the builder-inited event
    app.connect('builder-inited', generate_rst_from_json)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }


# Define our base template as a string
BASE_TEMPLATE = """
{{ title }}
{{ '=' * title|length }}

.. contents:: Table of Contents
   :depth: 3
   :backlinks: none

{% if 'description' in json_spec %}
Overview
--------
{{ json_spec.description }}
{% endif %}

{% if 'type' in json_spec %}
{% if is_list(json_spec.type) %}
:type: {{" | ".join(json_spec.type)}}
{% else %}
:type: {{"object" if json_spec.type == "assoc" else json_spec.type}}
{% endif %}
{% endif %}


{% if 'any_of' in json_spec %}
:One of:

{% for option in json_spec.any_of %}
- :doc:`{{ option.ref }}`
{% endfor %}
{% endif %}

{% for k, v in json_spec.items() %}
{% if k not in ['indices', 'any_of', 'type', 'description', 'additional_indices'] %}
:{{ k }}: {{ v if not is_list(v) else " | ".join(v) }}
{% endif %}
{% endfor %}

{% if 'indices' in json_spec %}
Properties
----------

{% for prop_name, prop_data in json_spec.indices | dictsort %}
{{ render_property(prop_name, prop_data, 1) }}
{% endfor %}
{% endif %}

{% if examples %}
Examples
--------
.. code-block:: json

{{ examples|indent(4, first=True) }}
{% endif %}
"""

# Property template as a macro
PROPERTY_TEMPLATE = """
{% macro render_property(name, data, depth) %}
{%- set header_chars = ['=', '-', '~', '^', '"'] %}
{{ name }}
{% if depth < 5 %}
{{ header_chars[depth + 1] * name|length }}
{% else %}
{{ '*' * depth }} {{ name }}
{% endif %}

{% if 'description' in data %}
{{data.description}}
{% endif %}

{% if 'type' in data %}
{% if is_list(data.type) %}
:type: {{" | ".join(data.type)}}
{% else %}
:type: {{"object" if data.type == "assoc" else data.type}}
{% endif %}
{% endif %}

{% if 'ref' in data %}
:ref: :doc:`{{data.ref}}`
{% endif %}

{% for key, value in data.items() if key not in ['description', 'type', 'indices', 'ref', 'additional_indices'] %}
:{{ key }}: {{ value if not is_list(value) else " | ".join(value) }}
{% endfor %}

{% if data.indices %}
Nested Properties:
{{ header_chars[depth + 2] * 'Nested Properties:'|length }}

{% for prop_name, prop_data in data.indices | dictsort %}
{{ render_property(prop_name, prop_data, depth + 1) }}
{% endfor %}

{% endif %}
{% endmacro %}
"""


def generate_sphinx_doc(json_spec: Dict[str, Any], title: str) -> str:
    """
    Generate Sphinx documentation from JSON specification using Jinja2 templates.

    Args:
        json_spec: Dictionary containing the object specification
        title: Title for the documentation page

    Returns:
        String containing the RST documentation
    """
    # Set up Jinja2 environment
    env = Environment(
        loader=BaseLoader(),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True
    )
    env.globals['is_list'] = lambda x: isinstance(x, list)

    # First register the property rendering macro
    env.from_string(PROPERTY_TEMPLATE)

    # Create the main template
    template = env.from_string(PROPERTY_TEMPLATE + BASE_TEMPLATE)

    # Render the template
    return template.render(
        json_spec=json_spec,
        title=title,
    )