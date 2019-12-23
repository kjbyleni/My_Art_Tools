from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

import ideas.factory as gen_factory
import practice.factory as practice_factory


class IdeasButton(Button):
    def get_environment(self):
        try:
            self.text = str(gen_factory.get_env().generate())
        except Exception:
            self.text = "Error"

    def get_character(self):
        try:
            self.text = str(gen_factory.get_character().generate())
        except Exception:
            self.text = "Error"

    def get_items(self):
        try:
            generated_items = ''
            items = gen_factory.get_items()
            for i in range(5):
                generated_items += f'{items.generate()} \n'
            self.text = str(generated_items)
        except Exception:
            self.text = "Error"

    def get_exercise(self):
        try:
            self.text = str(practice_factory.get_exercise().generate())
        except Exception:
            self.text = "Error"

    def get_study(self):
        try:
            self.text = str(practice_factory.get_study().generate())
        except Exception:
            self.text = "Error"


class ArtToolsIdeasContainer(GridLayout):
    pass


class ArtToolsApp(App):
    def build(self):
        return ArtToolsIdeasContainer()


if __name__ == '__main__':
    ArtToolsApp().run()
