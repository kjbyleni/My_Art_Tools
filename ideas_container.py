from kivy.uix.widget import Widget

import ideas.factory as gen_factory
import lib.utils as utils

class IdeasContainer(Widget):
    score = 'My Score Here'

    def get_all(self):
        return gen_factory.get_all().generate()
