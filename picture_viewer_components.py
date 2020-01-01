from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import (
    NumericProperty, ObjectProperty
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen

from ideas.image_manager import Images

MINUTES = 60


class PictureViewer(AnchorLayout):
    time_between = NumericProperty(0)
    file_path_key = ObjectProperty('')
    total_images_to_dislpay = NumericProperty(1)
    total_images_displayed = NumericProperty(1)
    images = ObjectProperty(None)
    clock_event = None

    def change_image(self, get_prev=False, get_next=False):
        for child in self.children:
            if child.source:
                if get_prev:
                    child.source = self.images.get_previous_image()
                elif get_next:
                    child.source = self.images.get_next_image()
                else:
                    child.source = self.images.get_rand_image()

    def change_gallery(self, path_key):
        self.images = Images(path_key=path_key)
        self.change_image()

    def load_art_tools_main(self):
        self.clock_event.cancel()
        self.total_images_displayed = 1
        self.parent.manager.current = "Kyle's Art Tools"

    def update_images(self, dt):
        if self.total_images_displayed < self.total_images_to_dislpay:
            self.change_image()
            self.total_images_displayed += 1
        else:
            self.load_art_tools_main()

    def setup_background(self, path_key):
        self.change_gallery(path_key=path_key)
        image = Image()
        image.source = self.images.get_rand_image()
        self.add_widget(image)

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
            elif args[key_value_index] == 8:  # Backspace Pressed!
                self.load_art_tools_main()


class PictureViewerScreen(Screen):
    pass
