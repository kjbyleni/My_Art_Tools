from lib.generator import Generator


class EnvironmentGenerator(Generator):
    def __init__(self):
        Generator.__init__(self, 'Environment')
        self.SEASON = 'season'
        self.TIME = 'time'
        self.INSIDE = 'inside'
        self.OUTSIDE = 'outside'
        self.keys = [self.SEASON, self.TIME, self.INSIDE, self.OUTSIDE]
