from kivy.app import App
from kivy.clock import Clock
from kivy.clock import mainthread
from kivy.core.window import Window
from kivy.properties import (
    NumericProperty, ObjectProperty
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

import ideas.factory as gen_factory
import practice.factory as practice_factory
from lib.utils import read_in_paths, add_folder_to_path, remove_folder_path
from practice.image_manager import Images

FIGURE_DRAWING_INDEX = 0
LANDSCAPE_DRAWING_INDEX = 1
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


class ImgViewerBtn(Button):
    file_key = ObjectProperty('')
    file_value = ObjectProperty('')

    def load_ref_drawing(self, *kwargs):
        my_parent = self.parent.parent.parent.parent.parent
        my_manager = self.parent.parent.parent.parent.parent.manager
        pic_viewer = my_manager.get_screen('Image Reference Viewer').ids.picture_viewer

        pic_viewer.time_between = my_parent.ids.time_between_images.text
        pic_viewer.total_images_to_dislpay = my_parent.ids.total_images_to_show.text
        pic_viewer.setup_background(self.text)
        my_manager.current = 'Image Reference Viewer'


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

    def add_path(self):
        add_folder_to_path()
        self.parent.parent.parent.update_buttons()


class ArtToolsIdeasContainer(GridLayout):
    pass


class DeleteButton(Button):
    def delete_with_key(self, *kwargs):
        remove_folder_path(self.id)
        self.parent.parent.parent.parent.parent.update_buttons()


class ArtToolsScreen(Screen):
    imgViewerBtns = ObjectProperty(ImgViewerBtn())
    img_paths = ObjectProperty('')
    loaded = ObjectProperty(False)

    @mainthread
    def on_enter(self):
        if not self.loaded:
            self.img_paths = read_in_paths()
            for key in self.img_paths:
                button = ImgViewerBtn(text=key)
                button.file_key = key
                button.file_value = self.img_paths[key]
                button.bind(on_press=button.load_ref_drawing)

                delete_btn = DeleteButton(text='D')
                delete_btn.id = key
                delete_btn.size_hint = (.25, 1)
                delete_btn.bind(on_press=delete_btn.delete_with_key)

                al = BoxLayout()
                al.padding = 10
                al.id = 'img_viewer_btn'
                al.add_widget(button)
                al.add_widget(delete_btn)
                self.ids.image_box.add_widget(al)
                self.loaded = True

    def update_buttons(self):
        for i in range(len(self.ids.image_box.children)):
            self.ids.image_box.remove_widget(self.ids.image_box.children[-1])

        self.loaded = False
        self.on_enter()


class ArtToolsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ArtToolsScreen())
        sm.add_widget(PictureViewerScreen())
        return sm


if __name__ == '__main__':
    ArtToolsApp().run()
