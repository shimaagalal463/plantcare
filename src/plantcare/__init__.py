"""plantcare — houseplant care tracker."""
__version__ = "1.2.0"
__author__ = "Shimaa Galal"

from .storage import Book, init_book
from .cli import main

__all__ = ["Book", "init_book", "main", "__version__"]
