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

from sphinx.addnodes import desc_signature

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "howso"
copyright = f"2019-{datetime.date.today().year}, Howso Incorporated"
author = "Howso Incorporated"
html_title = "Howso Engine Documentation"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_autodoc_typehints",
    "myst_parser",
    "sphinx.ext.doctest",
    "sphinx.ext.ifconfig",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxcontrib.images",
    "sphinx_reredirects",
    "matplotlib.sphinxext.plot_directive",
]

templates_path = ["_templates"]
exclude_patterns = ["build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# -- Internationalization ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization

language = "en"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")
html_context = {"howso_home_url": os.environ.get("HOWSO_HOME_URL")}
# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True
html_theme = "pydata_sphinx_theme"
html_favicon = "_static/favicon.ico"
html_logo = "_static/howso_logo_icon.svg"
html_show_sourcelink = False
html_theme_options = {
    "logo": {
        "text": "",
        "alt_text": "Howso",
        "image_dark": "_static/howso_logo_icon_white.svg",
    },
    "header_links_before_dropdown": 4,
    "icon_links": [
        {
            "name": "Howso Home",
            "url": os.environ.get("HOWSO_HOME_URL", "https://howso.com/"),
            "icon": "fa-solid fa-house",
            "type": "fontawesome",
        }
    ],
    "show_toc_level": 2,
}
html_static_path = [
    "_static",
]
html_css_files = [
    "css/theme.css",
    "css/custom.css",
]
html_js_files = ["js/html-js-class.js", "js/icon.js", "js/page-sidebar-secondary.js"]

master_doc = "index"

# -- Options for HTMLHelp output ---------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-help-output

htmlhelp_basename = "howsodoc"


# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "howso.tex", "Howso Engine", "Howso Incorporated", "manual"),
]

latex_logo = "_static/howso_logo_icon.svg"


# -- Options for manual page output ------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-manual-page-output

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "howso", "Howso Engine", [author], 1)]

# -- Options for Texinfo output ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-texinfo-output

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "howso",
        "Howso Engine",
        author,
        "howso",
        "One line description of project.",
        "Miscellaneous",
    ),
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
autodoc_typehints = "description"
autodoc_typehints_description_target = "all"

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

# Sphinx Autodoc Typestrings
# https://github.com/tox-dev/sphinx-autodoc-typehints?tab=readme-ov-file
always_use_bars_union = True
typehints_defaults = "comma"
always_document_param_types = True
simplify_optional_unions = True

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
    # "foo": "/bar.html" # Creates a redirect from "/foo.html" to "/bar.html"
    "user_guide/index.html": "/en/release-latest/user_guide/index.html",
    "user_guide/basic_capabilities/predictions.html": "/en/release-latest/user_guide/basic_capabilities/predictions.html",
    "getting_started/concepts.html": "https://docs.howso.com/en/release-latest/getting_started/concepts.html",
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


def _strip_types(app, what, name, obj, options, lines):
    """Strip lines which have types defined to force the plugin to generate them."""
    lines_to_remove = []
    for line in lines:
        if (
            ":type" in line or ":rtype" in line
        ) and ":sphinx_autodoc_typehints_type:" not in line:
            lines_to_remove.append(line)

    for line in lines_to_remove:
        lines.remove(line)


def setup(app):
    app.connect("object-description-transform", _wrap_signatures, priority=1000)
    app.connect("autodoc-process-docstring", _strip_types, priority=1000)
