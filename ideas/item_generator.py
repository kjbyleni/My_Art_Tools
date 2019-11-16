from lib.generator import Generator


class ItemGenerator(Generator):

    def __init__(self):
        self.ITEMS = 'items'
        keys = [self.ITEMS]
        Generator.__init__(self, context='Items', keys=keys)
