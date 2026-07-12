# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Dose-Aware and Robust Contour QA for Radiotherapy"
copyright = "2025-2026, Amith Kamath"
author = "Amith Kamath"

release = "0.1"
version = "0.1.0"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_book_theme",
    "myst_parser",
    "sphinxcontrib.bibtex",
]

myst_enable_extensions = [
    "dollarmath",  # $...$ and $$...$$ math in Markdown
]

# -- Bibliography (sphinxcontrib-bibtex)
bibtex_bibfiles = ["references.bib"]
bibtex_reference_style = "author_year"

# Some source .bib entries are missing optional fields (e.g. booktitle); don't
# turn those into build warnings for the website.
suppress_warnings = ["bibtex.missing_field"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

master_doc = "index"
source_suffix = [".rst", ".md"]

# -- Options for HTML output

html_theme = "sphinx_book_theme"

html_theme_options = {
    "navigation_depth": 4,  # Depth of nested TOC items
    "show_nav_level": 2,  # Show top-level items expanded
    "collapse_navigation": True,  # Collapse subsections by default
    "extra_footer": (
        '<div>This work is licensed under '
        '<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">'
        'CC BY-NC-ND 4.0</a>.</div>'
    ),
}

# -- Options for EPUB output
epub_show_urls = "footnote"
