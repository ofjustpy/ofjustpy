# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Kavya: A Full-Stack Web Development Framework in Python'
copyright = '2024, Kabira K.'
author = 'Kabira K.'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# import sphinx_readable_theme
# html_theme = 'readable'
# html_theme_path = [sphinx_readable_theme.get_html_theme_path()]
html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'

html_static_path = ['_static']

