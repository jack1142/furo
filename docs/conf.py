# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

#
# -- sys.path preparation ----------------------------------------------------
#

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "src"))

#
# -- Project information -----------------------------------------------------
#

project = "furo-issue-108-minimal-repro"
copyright = "doesn't matter"
author = "doesn't matter"

#
# -- General configuration ---------------------------------------------------
#

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    # 3rd-party extensions
    "furo",
]

#
# -- Options for HTML output -------------------------------------------------
#

html_theme = "furo"
html_title = "Furo - Issue 108 - minimal repro"
