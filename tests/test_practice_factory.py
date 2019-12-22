import practice.factory as practice_factory
from lib.utils import get_path

IDEA_PATH = f'{get_path(8)}//test_practice_ideas.txt'


def test_study_keys():
    study_obj = practice_factory.get_study(idea_path=IDEA_PATH)
    assert study_obj.keys == ['study', 'anatomy', 'emotion']


def test_study_context():
    study_obj = practice_factory.get_study(idea_path=IDEA_PATH)
    assert study_obj.context == 'Study'


def test_exercise_keys():
    exercise_obj = practice_factory.get_exercise(idea_path=IDEA_PATH)
    assert exercise_obj.keys == ['exercise']


def test_exercise_context():
    exercise_obj = practice_factory.get_exercise(idea_path=IDEA_PATH)
    assert exercise_obj.context == 'Exercise'
