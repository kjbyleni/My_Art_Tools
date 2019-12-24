import ideas.factory as gen_factory
import practice.factory as practice_factory
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty, ObjectProperty
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from practice.image_manager import Images

FIGURE_DRAWING_INDEX = 0
LANDSCAPE_DRAWING_INDEX = 1
MINUTES = 60


class PictureViewer(AnchorLayout):
    time_between = NumericProperty(0)
    file_index = NumericProperty(1)
    total_images_to_dislpay = NumericProperty(1)
    images_displayed = NumericProperty(1)
    images = ObjectProperty(None)
    clock_event = None

    def get_image_source(self):
        if self.images is None:
            self.images = Images(image_path_index=self.file_index)
        return self.images.get_rand_image()

    def change_image(self):
        for child in self.children:
            child.source = self.images.get_rand_image()

    def toggle_index(self):
        if self.file_index == 0:
            self.file_index = 1
            self.images = Images(image_path_index=self.file_index)
        else:
            self.file_index = 0
            self.images = Images(image_path_index=self.file_index)

    def update_images(self, dt):
        if self.images_displayed < self.total_images_to_dislpay:
            for child in self.children:
                child.source = self.images.get_rand_image()
            self.images_displayed += 1
        else:
            self.clock_event.cancel()
            self.images_displayed = 1
            self.parent.manager.current = "Kyle's Art Tools"

    def set_clock(self):
        self.time_between *= MINUTES
        self.clock_event = Clock.schedule_interval(callback=self.update_images, timeout=self.time_between)


class PictureViewerScreen(Screen):
    pass


class IdeasButton(Button):
    def get_environment(self):
        self.text = str(gen_factory.get_env().generate())

    def get_character(self):
        self.text = str(gen_factory.get_character().generate())

    def get_items(self):
        generated_items = ''
        items = gen_factory.get_items()
        for i in range(5):
            generated_items += f'{items.generate()} \n'
        self.text = str(generated_items)

    def get_exercise(self):
        self.text = str(practice_factory.get_exercise().generate())

    def get_study(self):
        self.text = str(practice_factory.get_study().generate())


class ArtToolsIdeasContainer(GridLayout):
    pass


class ArtToolsScreen(Screen):
    pass


class ArtToolsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ArtToolsScreen())
        sm.add_widget(PictureViewerScreen())
        return sm


if __name__ == '__main__':
    ArtToolsApp().run()
