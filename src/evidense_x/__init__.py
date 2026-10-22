"""
Evidense-X: Framework for Measuring Data Quality Defect Interactions in Machine Learning
"""

__version__ = "1.6.0"
__author__ = "Amit Singh Bhadouriya"
__license__ = "MIT"

from . import governance
from . import diagnostics
from . import remediation
from . import streaming

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    "governance",
    "diagnostics",
    "remediation",
    "streaming",
]
