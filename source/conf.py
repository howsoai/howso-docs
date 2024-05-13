# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import datetime
import os
from types import NoneType
from typing import Optional, Union, get_origin

from sphinx.ext import autodoc
from sphinx.addnodes import desc_signature

import howso.engine
import howso.engine.typing

from sphinx_autodoc_typehints import format_annotation

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'howso'
copyright = f'2019-{datetime.date.today().year}, Howso Incorporated'
author = 'Howso Incorporated'
html_title = 'Howso Engine Documentation'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.napoleon',
    'sphinx_autodoc_typehints',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'myst_parser',
    'sphinx.ext.doctest',
    'sphinx.ext.ifconfig',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinxcontrib.images',
    'sphinx_reredirects',
    'matplotlib.sphinxext.plot_directive',
]

templates_path = ['_templates']
exclude_patterns = ["build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# -- Internationalization ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization

language = "en"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_favicon = '_static/favicon.ico'
html_logo = '_static/howso_logo_icon.svg'
html_show_sourcelink = False
html_theme_options = {
    "logo": {
        "text": "",
        "alt_text": "Howso",
        "image_dark": '_static/howso_logo_icon_white.svg',
    },
    "header_links_before_dropdown": 4,
    "icon_links": [{
        "name": "Howso Home",
        "url": os.environ.get('HOWSO_HOME_URL', 'https://howso.com/'),
        "icon": "fa-solid fa-house",
        "type": "fontawesome"
    }],
    "show_toc_level": 2,
}
html_context = {
    'howso_home_url': os.environ.get('HOWSO_HOME_URL')
}
html_static_path = ['_static', ]
html_css_files = [
    'css/theme.css',
    'css/custom.css',
]
html_js_files = [
    'js/icon.js'
]

master_doc = 'index'

# -- Options for HTMLHelp output ---------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-help-output

htmlhelp_basename = 'howsodoc'


# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'howso.tex', 'Howso Engine',
     'Howso Incorporated', 'manual'),
]

latex_logo = '_static/howso_logo_icon.svg'


# -- Options for manual page output ------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-manual-page-output

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'howso', 'Howso Engine', [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-texinfo-output

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'howso', 'Howso Engine',
     author, 'howso', 'One line description of project.',
     'Miscellaneous'),
]

# -- Extension configuration -------------------------------------------------

# MyST-NB
# https://myst-nb.readthedocs.io/en/latest/

nb_execution_timeout = 600

# Sphinx Contrib Images
# https://sphinxcontrib-images.readthedocs.io/en/latest/
images_config = {
    "override_image_directive": True  # Force the `thumbnail` directive to override
    # the `image` directive, allowing for zooming when an image is clicked on.
}

# Autodoc
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
autodoc_class_signature = "mixed"
autodoc_inherit_docstrings = True
autodoc_member_order = "groupwise"
autodoc_typehints = "signature"

# Napoleon Conf
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#configuration
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = True
napoleon_use_keyword = True

# Autosummary Conf
# https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html#generating-stub-pages-automatically
# autosummary_imported_members = True
autosummary_generate = True
autosummary_ignore_module_all = False

# Autosectionlabel
# https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html#configuration
# autosectionlabel_prefix_document = True
# def process_signature(annotation, config):    
#     if not hasattr(annotation, "__args__") or not hasattr(annotation, "__origin__"):
#         return None

#     if (
#         annotation.__module__ == "typing" and
#         isinstance(annotation.__args__, tuple) and
#         len(annotation.__args__) == 2 and
#         annotation.__args__[1] == NoneType and
#         annotation.__origin__ == Union
#     ):
#         new_annotation = annotation.__args__[0]
#         formatted = format_annotation(new_annotation, config)
#         formatted += ", optional"
#         return formatted

# Redirects
# https://documatt.com/sphinx-reredirects/usage.html
redirects = {
    # "foo": "/bar.html" Creates a redirect from "/foo.html" to "/bar.html"
}

# -- Documentation Setup -----------------------------------------------------

def _wrap_signatures(app, domain, objtype, content) -> None:
    """Add css class to signatures that exceed 60 characters."""
    env = app.env
    assert env is not None
    signatures = content.parent[:-1]
    for signature in signatures:
        if isinstance(signature, desc_signature):
            signature_text = signature.astext()
            if len(signature_text) > 60:
                signature["classes"].append("sig-wrap")


def setup(app):
    app.connect("object-description-transform",
                _wrap_signatures, priority=1000)
