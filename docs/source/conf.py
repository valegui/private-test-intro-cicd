# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Introduccion a CI/CD"
copyright = "2023, valegui"
author = "valegui"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Include documentation from docstrings
    "sphinx.ext.napoleon",  # Support for NumPy adn Google style docstrings
    "sphinx.ext.githubpages",  # Publish HTML docs in GitHub Pages
    "sphinx.ext.doctest",  # Test snippets in the documentation
    "sphinx.ext.graphviz",
    "autoapi.extension",
]

# Autoapi settings
autoapi_type = "python"
autoapi_dirs = ["../../drinks"]
autoapi_file_patterns = ["*.py"]
autoapi_add_toctree_entry = False
autoapi_options = [
    "members",
    "private-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "imported-members",
    "show-inheritance-diagram",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "es"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_theme_options = {"navbar_start": ["logo-square"], "footer_start": ["footer"]}
