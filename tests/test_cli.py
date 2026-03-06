"""CLI 测试"""
from click.testing import CliRunner
from rag_reference_checker.cli import cli


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "RAG Reference Checker" in result.output


def test_check_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["check", "--help"])
    assert result.exit_code == 0
