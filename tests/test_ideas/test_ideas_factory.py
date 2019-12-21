import ideas.factory as idea_factory

IDEA_PATH = './test_generator_data/test_ideas.txt'


def test_items_keys():
    item_obj = idea_factory.get_items(idea_path=IDEA_PATH)
    assert item_obj.keys == ['items']


def test_items_context():
    item_obj = idea_factory.get_items(idea_path=IDEA_PATH)
    assert item_obj.context == 'Items'


def test_character_keys():
    char_obj = idea_factory.get_character(idea_path=IDEA_PATH)
    assert char_obj.keys == ['shapes', 'physical nature', 'distinguishing characteristic']


def test_character_context():
    char_obj = idea_factory.get_character(idea_path=IDEA_PATH)
    assert char_obj.context == 'Character'


def test_env_keys():
    env_obj = idea_factory.get_env(idea_path=IDEA_PATH)
    assert env_obj.keys == ['season', 'time', 'inside', 'outside']


def test_env_context():
    env_obj = idea_factory.get_env(idea_path=IDEA_PATH)
    assert env_obj.context == 'Environment'


def test_get_all():
    all_obj = idea_factory.get_all(idea_path=IDEA_PATH)
    assert all_obj.context == 'general'
