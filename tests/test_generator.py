import pytest
import os
import random
import subprocess

from lib.generator import Generator


KEYS = ['shapes', 'physical nature', 'distinguishing characteristic', 'items', 'season', 'time', 'inside', 'outside']


@pytest.fixture
def gen():
    return Generator(gen_path="./test_generator_data/test_ideas.txt")


def test_init_default_context(gen):
    assert gen.context == 'general'


def test_init_message(gen):
    assert gen.message is not None


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


def test_generate(gen):
    expected = ['Oval', 'Bird', 'Kung Fu Master', 'Clouds', 'Winter', 'Night', 'Space Shuttle', 'Wetland']
    random.seed(1)
    gen.generate()
    assert gen.rand_items == expected


def test_export_unique_path():
    export_file_path = './test_generator_data/exported.txt'
    assert not os.path.exists(export_file_path)

    gen = Generator(gen_path='./test_generator_data/tst_export.txt')
    gen.export_lst(export_file_path)
    assert os.path.exists(export_file_path)

    os.remove(export_file_path)


def test_export_default_path():
    original_path = './test_generator_data/original.txt'
    assert os.path.exists(original_path)

    gen = Generator(gen_path=original_path)
    os.remove(original_path)

    assert not os.path.exists(original_path)
    gen.export_lst()

    assert os.path.exists(original_path)


def test_convert_file_to_array():
    expected = ['Hello', 'Please', 'Convert', 'Me', 'To', 'Array']
    converted_file = Generator.convert_file_to_array('./test_generator_data/file_to_convert_to_array.txt')
    assert expected == converted_file
