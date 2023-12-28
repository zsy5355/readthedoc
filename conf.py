# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'read'
copyright = '2023, zsy'
author = 'zsy'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = []
extensions = ["myst_parser"]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

#import os
#import sphinx_rtd_theme

# 使用环境变量 READTHEDOCS_OUTPUT 设置输出路径

# 使用默认的输出路径
#html_path = '_build/html'

# 设置输出路径


# 设置输出路径
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
#html_static_path = [os.path.join(html_path, 'static')]
