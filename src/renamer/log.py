import logging
from typing import Optional

from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.logging import RichHandler

from . import identifier

## <% based on entangled.py/logging.py (2024-01-07)

# Singleton type flag, to prevent running `init()` twice
_SETUP: bool = False


class BackTickHighlighter(RegexHighlighter):
    """
    Highlight text between backticks for emphasis in logged text.
    """

    highlights = [r"`(?P<bold>[^`]*)`"]


class WhitespaceStrippingConsole(Console):
    """
    Remove white space from the ends of logged text.

    Snippet from https://github.com/Textualize/rich/issues/2647#issuecomment-1324286428
    """

    def _render_buffer(self, *args, **kwargs) -> str:
        """
        Ensure the text lines ends with a `\n` without spaces before it.

        Returns:
            str: text without spaces at the end
        """
        rendered = super()._render_buffer(*args, **kwargs)
        newline_char = "\n" if rendered[-1] == "\n" else ""
        return (
            "\n".join(line.rstrip() for line in rendered.splitlines())
            + newline_char
        )


# Global rich console object
console: Console = WhitespaceStrippingConsole()


def init(debug: Optional[bool] = False) -> None:
    """
    Set the basicConfig details.

    Args:
        debug (bool, optional)
        :   Log level to `logging.DEBUG`.
            Defaults to False and thus `logging.INFO`.
    """
    global _SETUP
    if _SETUP:
        return

    if debug:
        level = logging.DEBUG
    else:
        level = logging.INFO

    FORMAT = "%(message)s"
    logging.basicConfig(
        level=level,
        format=FORMAT,
        datefmt="[%X]",
        handlers=[
            RichHandler(
                show_path=debug,
                highlighter=BackTickHighlighter(),
                console=console,
                rich_tracebacks=debug,
            )
        ],
    )
    log = logging.getLogger(__package__)
    log.debug(f"Logging for {identifier(True)} at debug level")

    _SETUP = True


def logger() -> logging.Logger:
    if not _SETUP:
        init()

    return logging.getLogger(__package__)


## %>
