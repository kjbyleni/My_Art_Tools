from lib.generator import Generator


class EnvironmentGenerator(Generator):
    def __init__(self):
        self.SEASON = 'season'
        self.TIME = 'time'
        self.INSIDE = 'inside'
        self.OUTSIDE = 'outside'
        keys = [self.SEASON, self.TIME, self.INSIDE, self.OUTSIDE]
        Generator.__init__(self, context='Environment', keys=keys)
