from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import (
    NumericProperty, ObjectProperty
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

import ideas.factory as gen_factory
import practice.factory as practice_factory
from practice.image_manager import Images

FIGURE_DRAWING_INDEX = 0
LANDSCAPE_DRAWING_INDEX = 1
MINUTES = 60


class PictureViewer(AnchorLayout):
    time_between = NumericProperty(0)
    file_index = NumericProperty(1)
    total_images_to_dislpay = NumericProperty(1)
    total_images_displayed = NumericProperty(1)
    images = ObjectProperty(None)
    clock_event = None

    def get_image_source(self):
        if self.images is None:
            self.images = Images(image_path_index=self.file_index)
        return self.images.get_rand_image()

    def change_image(self, get_prev=False, get_next=False):
        for child in self.children:
            if child.source:
                if get_prev:
                    child.source = self.images.get_previous_image()
                elif get_next:
                    child.source = self.images.get_next_image()
                else:
                    child.source = self.images.get_rand_image()

    def change_gallery(self, index):
        self.images = Images(image_path_index=index)
        self.change_image()

    def toggle_index(self, gallery):
        if gallery == 'Landscape Drawing':
            self.file_index = LANDSCAPE_DRAWING_INDEX
            self.change_gallery(self.file_index)
        elif gallery == 'Figure Drawing':
            self.file_index = FIGURE_DRAWING_INDEX
            self.change_gallery(self.file_index)

    def update_images(self, dt):
        if self.total_images_displayed < self.total_images_to_dislpay:
            self.change_image()
            self.total_images_displayed += 1
        else:
            self.clock_event.cancel()
            self.total_images_displayed = 1
            self.parent.manager.current = "Kyle's Art Tools"

    def set_clock(self):
        self.time_between *= MINUTES
        self.clock_event = Clock.schedule_interval(callback=self.update_images, timeout=self.time_between)
        self.bound_window = Window.bind(on_key_down=self.key_action)

    def key_action(self, *args):
        print(args)
        char_key_index = 3
        if args[char_key_index] == ' ':  # Spacebar was pressed!
            self.change_image()
            self.clock_event.cancel()
            self.clock_event = Clock.schedule_interval(callback=self.update_images, timeout=self.time_between)
        elif args[char_key_index] is None:
            key_value_index = 1
            if args[key_value_index] == 276:  # Left Arrow Pressed!
                self.change_image(get_prev=True)
                self.clock_event.cancel()
                self.clock_event = Clock.schedule_interval(callback=self.update_images, timeout=self.time_between)
            elif args[key_value_index] == 275:  # Right Arrow Pressed!
                self.change_image(get_next=True)
                self.clock_event.cancel()
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
            generated_items += items.generate()
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
