# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
# sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('../../leila'))


# -- Project information -----------------------------------------------------

project = 'LEILA'
copyright = '2021, UCD - DNP'
author = 'UCD - DNP'

# The full version, including alpha/beta/rc tags
release = '0.2'
version = 'latest'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosectionlabel', 'sphinx_copybutton', 'sphinx_multiversion']
# extensions = ['sphinx.ext.autodoc', 'rinoh.frontend.sphinx','sphinx.ext.autosectionlabel', 'sphinx_copybutton']

copybutton_prompt_text = "myinputprompt"
copybutton_prompt_text = ">>> "

# copybutton_prompt_text = r">>> |\.\.\. |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
# copybutton_prompt_is_regexp = True
# copybutton_only_copy_prompt_lines = False

rinoh_documents = [('index',                                      # top-level file (index.rst)
                    'Documentacion',                              # output (target.pdf)
                    'Documentacion librería calidad de datos',    # document title
                    'DNP - UCD')]                                 # document author  

# latex_elements = {'classoptions': ',openany', 'babel': r'\usepackage[english]{babel}'}
latex_elements = {'classoptions': ',openany', 'babel': r'\usepackage[spanish]{babel}'}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'es'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_show_sourcelink = False

html_context = {
    "display_github": False,        # Integrate GitHub
    "github_user": "ucd-dnp",       # Username
    "github_repo": "leila",         # Repo name
    "github_version": "master",     # Version
    "conf_py_path": "/source/",     # Path in the checkout to the docs root
}


html_theme_options = {    
    'display_version': True,
    'style_external_links' : True    
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/custom.css']
html_logo  = '_static/image/logo_400.png'
html_favicon = '_static/image/favicon.ico'

from sphinx.writers.html import HTMLTranslator
class PatchedHTMLTranslator(HTMLTranslator):
    def visit_reference(self, node):
        if node.get('newtab') or not (node.get('target') or node.get('internal') or 'refuri' not in node):
            node['target'] = '_blank'
        super().visit_reference(node)

def setup(app):
    app.set_translator('html', PatchedHTMLTranslator)