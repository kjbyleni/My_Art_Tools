from lib.generator import Generator


class PracticeGenerator(Generator):
    def __init__(self, context='general', keys=[], idea_path='./practice/practice_ideas.txt'):
        Generator.__init__(self, context=context, keys=keys, idea_path=idea_path)


def get_study():
    study = 'study'
    anatomy = 'anatomy'
    emotion = 'emotion'
    keys = [study, anatomy, emotion]
    return PracticeGenerator(context='study', keys=keys)


def get_exercise():
    exercise = 'exercise'
    keys = [exercise]
    return PracticeGenerator(context='exercise', keys=keys)

