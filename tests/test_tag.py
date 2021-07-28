import pytest

from common_pyutil.decorators import Tag

tag = Tag("bleh")


@tag
def some_func():
    pass


@tag
def some_other_func():
    pass


def test_tag_name():
    assert tag.name == "bleh"


def test_tag_names():
    assert tag.names == ["some_func", "some_other_func"]


def test_tag_members():
    assert tag.members == {"some_func": some_func,
                           "some_other_func": some_other_func}
