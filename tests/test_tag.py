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


def test_tag_add_remove():
    tag.remove("some_func")
    assert tag.members == {"some_other_func": some_other_func}
    tag.add(some_func)
    assert tag.members == {"some_func": some_func,
                           "some_other_func": some_other_func}
    assert "some_func" in tag
    assert "random" not in tag
