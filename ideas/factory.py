from lib.generator import Generator

IDEA_PATH = './ideas/ideas.json'


def get_items(idea_path=IDEA_PATH):
    items = 'items'
    keys = [items]
    return Generator(context='Items', keys=keys, idea_path=idea_path)


def get_character(idea_path=IDEA_PATH):
    shape = 'shapes'
    nature = 'physical nature'
    characteristic = 'distinguishing characteristic'
    keys = [shape, nature, characteristic]
    return Generator(context='Character', keys=keys, idea_path=idea_path)


def get_env(idea_path=IDEA_PATH):
    season = 'season'
    time = 'time'
    inside = 'inside'
    outside = 'outside'
    keys = [season, time, inside, outside]
    return Generator(context='Environment', keys=keys, idea_path=idea_path)


def get_study(idea_path=IDEA_PATH):
    study = 'study'
    anatomy = 'anatomy'
    emotion = 'emotion'
    keys = [study, anatomy, emotion]
    return Generator(context='Study', keys=keys, idea_path=idea_path)


def get_exercise(idea_path=IDEA_PATH):
    exercise = 'exercise'
    keys = [exercise]
    return Generator(context='Exercise', keys=keys, idea_path=idea_path)


def get_all(idea_path=IDEA_PATH):
    return Generator(context='Practice', idea_path=idea_path)

