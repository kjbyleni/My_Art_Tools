from lib.generator import Generator


class PracticeGenerator(Generator):
    def __init__(self, context='general', keys=[], idea_path='./practice/practice_ideas.txt'):
        Generator.__init__(self, context=context, keys=keys, idea_path=idea_path)


IDEA_PATH = './practice/practice_ideas.txt'


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

