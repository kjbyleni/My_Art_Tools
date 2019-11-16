from lib.generator import Generator


class PracticeGenerator(Generator):
    def __init__(self, idea_path: str, context='general', keys=[]):
        Generator.__init__(self, context=context, keys=keys, idea_path=idea_path)


IDEA_PATH = './practice/practice_ideas.json'


def get_study(idea_path=IDEA_PATH):
    study = 'study'
    anatomy = 'anatomy'
    emotion = 'emotion'
    keys = [study, anatomy, emotion]
    return PracticeGenerator(context='Study', keys=keys, idea_path=idea_path)


def get_exercise(idea_path=IDEA_PATH):
    exercise = 'exercise'
    keys = [exercise]
    return PracticeGenerator(context='Exercise', keys=keys, idea_path=idea_path)

