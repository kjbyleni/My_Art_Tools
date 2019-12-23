from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from ideas_container import IdeasContainer


class ArtTools(Widget):
    ideas = ObjectProperty(None)
    pass


class ArtToolsApp(App):
    def build(self):
        return ArtTools()


if __name__ == '__main__':
    ArtToolsApp().run()
