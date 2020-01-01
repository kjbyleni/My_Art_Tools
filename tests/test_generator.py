import pytest

from ideas.generator import Generator

KEYS = ['shapes', 'physical nature', 'distinguishing characteristic', 'items', 'season', 'time', 'inside', 'outside',
        'exercise', 'study', 'anatomy', 'emotion']


@pytest.fixture
def gen():
    yield Generator()


def test_init_default_context(gen):
    assert gen.context == 'general'


def test_init_rand_items(gen):
    assert len(gen.rand_items) == 0


def test_lst_matches_keys(gen):
    assert gen.get_keys() == KEYS


def test_lst_keys_are_found(gen):
    for key in KEYS:
        assert key in gen.lst


def test_lst_keys_return_arrays(gen):
    for key in KEYS:
        assert len(gen.lst[key]) > 0


def test_convert_file_to_array():
    expected = ['Hello', 'Please', 'Convert', 'Me', 'To', 'Array']
    converted_file = Generator.convert_file_to_array(f'.\\tests\\file_to_convert_to_array.txt')
    assert expected == converted_file
