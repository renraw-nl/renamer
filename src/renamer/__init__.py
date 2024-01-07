from importlib.metadata import version
from typing import Optional

__version__ = version(__package__)


def identifier(ticks: Optional[bool] = False) -> str:
    """
    Package name with version.

    Returns:
        str: packega with version
    """
    if ticks:
        ticks = "`"
    else:
        ticks = ""

    return f"{ticks}{__package__}{ticks} (v{__version__})"


del version
