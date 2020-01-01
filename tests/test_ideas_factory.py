import ideas.factory as idea_factory
import os


def test_items_keys():
    item_obj = idea_factory.get_items()
    assert item_obj.keys == ['items']


def test_items_context():
    item_obj = idea_factory.get_items()
    assert item_obj.context == 'Items'


def test_character_keys():
    char_obj = idea_factory.get_character()
    assert char_obj.keys == ['shapes', 'physical nature', 'distinguishing characteristic']


def test_character_context():
    char_obj = idea_factory.get_character()
    assert char_obj.context == 'Character'


def test_env_keys():
    env_obj = idea_factory.get_env()
    assert env_obj.keys == ['season', 'time', 'inside', 'outside']


def test_env_context():
    env_obj = idea_factory.get_env()
    assert env_obj.context == 'Environment'


def test_study_keys():
    env_obj = idea_factory.get_study()
    assert env_obj.keys == ['study', 'anatomy', 'emotion']


def test_study_context():
    env_obj = idea_factory.get_study()
    assert env_obj.context == 'Study'


def test_exercise_keys():
    env_obj = idea_factory.get_exercise()
    assert env_obj.keys == ['exercise']


def test_exercise_context():
    env_obj = idea_factory.get_exercise()
    assert env_obj.context == 'Exercise'

