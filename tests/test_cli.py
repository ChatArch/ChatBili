import click
from click.testing import CliRunner

from chatbili import __version__
from chatbili.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatbili, version {__version__}" in result.output


def _add_signature_command(monkeypatch):
    @click.command("inspect")
    @click.argument("item")
    @click.option("--format", "output_format", default="text", help="Output format.")
    def inspect_item(item, output_format):
        """Inspect an item."""

    monkeypatch.setitem(main.commands, "inspect", inspect_item)


def test_tree_option_prints_registered_cli_tree_with_signatures(monkeypatch):
    _add_signature_command(monkeypatch)
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0, result.output
    assert result.output == (
        "chatbili\n"
        "├── --help  # Show this message and exit.\n"
        "├── --version  # Show the version and exit.\n"
        "├── --tree  # Print the registered CLI tree and exit.\n"
        "├── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.\n"
        "└── inspect <ITEM> [--format OUTPUT-FORMAT]  # Inspect an item.\n"
    )


def test_tree_brief_omits_signatures_but_keeps_commands_and_descriptions(monkeypatch):
    _add_signature_command(monkeypatch)
    result = CliRunner().invoke(main, ["--tree-brief"])

    assert result.exit_code == 0, result.output
    assert result.output == (
        "chatbili\n"
        "├── --help  # Show this message and exit.\n"
        "├── --version  # Show the version and exit.\n"
        "├── --tree  # Print the registered CLI tree and exit.\n"
        "├── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.\n"
        "└── inspect  # Inspect an item.\n"
    )
