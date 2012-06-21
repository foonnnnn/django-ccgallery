# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.abspath('_themes'))

# -- General configuration -----------------------------------------------------

extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'ccgallery'
copyright = u'2012, c&c Design Consultants LTD.'
version = '0.0.1'
release = '0.0.1'
exclude_patterns = ['_build']
pygments_style = 'monokai'

# -- Options for HTML output ---------------------------------------------------

html_theme = 'cc'
html_theme_path = ['_themes']
html_short_title = 'ccgallery'
html_static_path = ['_static']
htmlhelp_basename = 'ccgallerydoc'
html_sidebars = {
    'index': ['sidebarintro.html',],
    '**': ['sidebarintro.html', 'localtoc.html'],
}


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
}
latex_documents = [
  ('index', 'ccgallery.tex', u'ccgallery Documentation',
   u'c\\&c Design Consultants LTD', 'manual'),
]

# -- Options for manual page output --------------------------------------------

man_pages = [
    ('index', 'ccgallery', u'ccgallery Documentation',
     [u'c&c Design Consultants LTD'], 1)
]

# -- Options for Texinfo output ------------------------------------------------

texinfo_documents = [
  ('index', 'ccgallery', u'ccgallery Documentation',
   u'c&c Design Consultants LTD', 'ccgallery', 'One line description of project.',
   'Miscellaneous'),
]
