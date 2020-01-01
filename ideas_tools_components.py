from kivy.clock import mainthread
from kivy.properties import (
    ObjectProperty
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

import ideas.factory as gen_factory
from ideas.utils import read_in_paths, add_folder_to_path, remove_folder_path


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
        self.text = str(gen_factory.get_exercise().generate())

    def get_study(self):
        self.text = str(gen_factory.get_study().generate())

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
