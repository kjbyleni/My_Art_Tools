from lib.generator import Generator


class CharacterGenerator(Generator):

    def __init__(self):
        Generator.__init__(self, 'Character')
        self.SHAPES = 'shapes'
        self.PHY_NATURE = 'physical nature'
        self.DIST_CHAR = 'distinguishing characteristic'
        self.keys = [self.SHAPES, self.PHY_NATURE, self.DIST_CHAR]

    def generate(self):
        self.get_rand_item(self.SHAPES)
        self.get_rand_item(self.SHAPES)
        self.get_rand_item(self.PHY_NATURE)
        self.get_rand_item(self.DIST_CHAR)
        self.print_result()
