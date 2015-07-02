#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import shlex

import sphinx_rtd_theme


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = 'prnd-notifications'
copyright = '2015, Suchan An <dobestan@prnd.co.kr>'
author = 'Suchan An <dobestan@prnd.co.kr>'

version = '0.1.0'
release = '0.1.0'

language = 'ko'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

todo_include_todos = False


html_theme = 'sphinx_rtd_theme'

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']

htmlhelp_basename = 'prnd-notificationsdoc'


latex_elements = {}

latex_documents = [
    (
        master_doc,
        'prnd-notifications.tex',
        'prnd-notifications Documentation',
        'Suchan An \\textless{}dobestan@prnd.co.kr\\textgreater{}',
        'manual'
    ),
]

man_pages = [
    (
        master_doc,
        'prnd-notifications', 'prnd-notifications Documentation',
        [author],
        1
    )
]

texinfo_documents = [
    (
        master_doc,
        'prnd-notifications',
        'prnd-notifications Documentation',
        author,
        'prnd-notifications',
        'One line description of project.',
        'Miscellaneous'
    ),
]

intersphinx_mapping = {'https://docs.python.org/': None}
