import pytest
from ideas.image_manager import PreviousArray

@pytest.fixture
def prev():
    p = PreviousArray()
    p.append("one")
    p.append("two")
    p.append("three")
    yield p


def test_initialize():
    p = PreviousArray()
    assert p.prev_index is None
    assert len(p.items) == 0


def test_append():
    p = PreviousArray()
    p.append("hello")
    assert len(p.items) == 1
    assert p.items[0] == 'hello'


def test_get_previous_no_items():
    p = PreviousArray()
    assert p.get_previous() is None


def test_get_previous_one_item():
    p = PreviousArray()
    p.append("one")
    assert p.get_previous() == 'one'


def test_get_previous_two_items():
    p = PreviousArray()
    p.append("one")
    p.append("two")
    assert p.get_previous() == 'one'


def test_get_previous_three_items(prev):
    assert prev.get_previous() == 'two'


def test_get_previous_called_twice(prev):
    prev.get_previous()
    assert prev.get_previous() == 'one'


def test_get_previous_called_more_than_length_of_items(prev):
    assert len(prev.items) == 3
    prev.get_previous()
    prev.get_previous()
    assert prev.get_previous() == 'one'


def test_get_first_resets_prev_index(prev):
    prev.get_previous()
    prev.get_previous()
    assert prev.get_first() == 'three'
    assert prev.prev_index is None


def test_empty_item_list_get_first_returns_none():
    p = PreviousArray()
    assert p.get_first() is None


def test_get_next_end_of_items():
    p = PreviousArray()
    assert p.get_next() is None


def test_get_next_one_item_in_list():
    p = PreviousArray()
    p.append('apple')
    assert p.get_next() == 'apple'


def test_get_next_prev_is_none(prev):
    assert prev.get_next() == 'three'


def test_get_next_after_get_prev(prev):
    prev.get_previous()
    assert prev.get_next() == 'three'


def test_get_next_after_get_prev_end_of_list(prev):
    prev.get_previous()
    prev.get_next()
    prev.get_next()
    assert prev.get_next() == 'three'


def test_get_next_when_prev_index_is_negative(prev):
    prev.prev_index = -5
    assert prev.get_next() == 'two'


def test_get_previous_when_index_is_larger_than_item_lenght(prev):
    prev.prev_index = 20
    assert prev.get_previous() == 'two'
