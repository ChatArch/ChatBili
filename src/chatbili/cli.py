"""CLI entrypoint for chatbili."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatbili import __version__


@click.group(invoke_without_command=True, no_args_is_help=True)
@click.version_option(__version__, prog_name="chatbili")
@add_tree_option(renderer_options={"root_name": "chatbili"})
def main() -> None:
    """chatbili command line interface."""
    # Add package-specific commands here. Prefer ChatStyle helpers for
    # interactive input when a command needs recoverable user input.


if __name__ == "__main__":
    main()
