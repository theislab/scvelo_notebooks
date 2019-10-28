project = 'scVelo'
author = 'Volker Bergen'
copyright = '2018, Volker Bergen'

version = ''
release = version

extensions = ['nbsphinx', 'sphinx_copybutton']

templates_path = ['_templates']
source_suffix = ['.rst', '.ipynb']
master_doc = 'index'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']
pygments_style = 'sphinx'


# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_options = dict(navigation_depth=2, titles_only=True)
html_context = dict(display_github=True, github_user='theislab', github_repo='scvelo_notebooks',
                    github_version='master', conf_py_path='/')

html_static_path = ['_static']


def setup(app):
    app.add_stylesheet('css/custom.css')
