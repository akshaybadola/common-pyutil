import pytest
import argparse
from common_pyutil.system import hierarchical_parser


def a_cmd(arglist):
    parser = argparse.ArgumentParser("a_cmd")
    parser.add_argument("-meow")
    args = parser.parse_args(arglist)
    print(args.__dict__)


def b_cmd(arglist):
    parser = argparse.ArgumentParser("b_cmd")
    parser.add_argument("--bow")
    args = parser.parse_args(arglist)
    print(args.__dict__)


def test_parser_exists_without_cmd(capsys):
    cmd_map = {"a": a_cmd, "b": b_cmd}
    parser = hierarchical_parser("test", 'test command [options]', cmd_map)
    with pytest.raises(SystemExit) as e:
        parser()
    assert e.type == SystemExit
