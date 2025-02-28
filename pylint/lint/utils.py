from __future__ import annotations
import contextlib
import platform
import sys
import traceback
from collections.abc import Iterator, Sequence
from datetime import datetime
from pathlib import Path
from pylint.constants import PYLINT_HOME, full_version

@contextlib.contextmanager
def augmented_sys_path(additional_paths: Sequence[str]) -> Iterator[None]:
    """Augment 'sys.path' by adding non-existent entries from additional_paths."""
    pass

def _is_relative_to(self: Path, *other: Path) -> bool:
    """Checks if self is relative to other.

    Backport of pathlib.Path.is_relative_to for Python <3.9
    TODO: py39: Remove this backport and use stdlib function.
    """
    pass