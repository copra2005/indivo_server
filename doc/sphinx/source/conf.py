# -*- coding: utf-8 -*-
#
# Indivo X documentation build configuration file, created by
# sphinx-quickstart on Wed Jul 20 17:33:59 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../')) # indivo_server/doc/sphinx
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../../')) # indivo_server/doc
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../../../')) # indivo_server

# Make sure we can grab Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'indivo.settings'

# Mock packages that we don't need so that code imports work
# on systems without the packages
mocks = ['markdown', 'markdown.preprocessors.Preprocessor', 'mardown.Extension',  'rdflib.collection', 'rdflib.exceptions.UniquenessError']
class Mock(object):
    def __init__(self, *args, **kwargs):
        pass

    def __getattr__(self, name):
        return Mock()

    def __call__(self, *args, **kwargs):
        return Mock()

for mod_name in mocks:
    sys.modules[mod_name] = Mock()

# SPECIAL SETUP FOR READTHEDOCS.ORG
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    
    # Use a special rtd.org settings module
    os.environ['DJANGO_SETTINGS_MODULE'] = 'indivo.settings_rtfd'

    # generate the autocode and the api-reference
    from django.core.management import call_command
    call_command('generate_docs', 'prepare')

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'localext.httpdomain']

# autodoc config
autodoc_default_flags = ['members', 
                         'undoc-members', 
                         'private-members', 
                         'show-inheritance',]
# todo config
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Indivo X'
copyright = u"2012, Children's Hospital Boston. All rights reserved"

from version import INDIVO_SERVER_VERSION, INDIVO_SERVER_RELEASE
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = INDIVO_SERVER_VERSION
# The full version, including alpha/beta/rc tags.
release = INDIVO_SERVER_RELEASE

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['indivo.views.', 'views.']

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
#    'rightsidebar':True,
#    'externalrefs': False,
    'footerbgcolor':'#1E3467',
    'footertextcolor':'#9EADCF',
    'sidebarbgcolor':'#294FAB',
    'sidebartextcolor':'#9EADCF',
#    'sidebarlinkcolor':'#1E3467',
    'sidebarlinkcolor':'#DDDDEE',
    'relbarbgcolor':'#1E3467',
    'relbartextcolor':'#9EADCF',
    'relbarlinkcolor':'#8CA0CF',
    'bgcolor': '#FEFCF7',
#    'textcolor':'black',
#    'linkcolor':'#1E3467',
#    'visitedlinkcolor':'#596E9D',
    'headbgcolor':'#BFC4CE',
    'headtextcolor':'#1E3467',
    'headlinkcolor':'#1E3467',
    }

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []
html_theme_path = [".theme"]

# The name for this set of Sphinx documents.  If None, it defaults to
html_title = "%s v%s documentation"%(project, version)
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['.static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'IndivoXdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'IndivoX.tex', u'Indivo X Documentation',
   u'Daniel Haas, Ben Adida, Arjun Sanyal, Isaac Kohane, Kenneth Mandl', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'indivox', u'Indivo X Documentation',
     [u'Daniel Haas, Ben Adida, Arjun Sanyal, Isaac Kohane, Kenneth Mandl'], 1)
]
