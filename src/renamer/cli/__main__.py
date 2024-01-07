import sys

import argh  # type: ignore
from rich_argparse import RichHelpFormatter

from .. import identifier, log

# from . import new, status, stitch, sync, tangle, watch, brei
# from ..errors.internal import bug_contact
# from ..errors.user import HelpfulUserError, UserError
# from . import help

## <% based on entangled.py/main.py (2024-01-07)


def main() -> None:
    """
    Renamer CLI entry point.
    """
    try:
        # Would be nice to have a help message
        # There
        parser = argh.ArghParser(formatter_class=RichHelpFormatter)
        parser.add_argument(
            "-d", "--debug", action="store_true", help="enable debug messages"
        )
        parser.add_argument(
            "-v",
            "--version",
            action="version",
            version=identifier(True),
            help="show version and exit",
        )
        # argh.add_commands(parser, functions=[])
        args = parser.parse_args()

        log.init(args.debug)
        log.logger().debug("Starting")

        # argh.dispatch(parser)
    except KeyboardInterrupt:
        log.logger().info("Stopping...")
        sys.exit(0)


if __name__ == "__main__":
    main()

## %>
