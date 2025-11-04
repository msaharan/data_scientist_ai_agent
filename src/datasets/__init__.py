"""Dataset abstractions and loader registry for tabular sources."""

from .base import DataSource, load_dataset
from .catalog import DatasetCatalog, load_catalog
from .loaders import (
    DataFormat,
    DatasetLoader,
    detect_format_from_path,
    get_loader_for_format,
    register_loader,
)

__all__ = [
    "DataFormat",
    "DatasetLoader",
    "DataSource",
    "DatasetCatalog",
    "detect_format_from_path",
    "get_loader_for_format",
    "load_dataset",
    "load_catalog",
    "register_loader",
]

