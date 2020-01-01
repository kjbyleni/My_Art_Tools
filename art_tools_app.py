from kivy.app import App
from kivy.clock import mainthread
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

from ideas.ideas_tools_components import ArtToolsScreen
from lib.generator import Generator
from practice.picture_viewer_components import PictureViewerScreen


class EditButton(Button):
    def load_edit_screen(self):
        my_manager = self.parent.parent.parent.manager
        my_manager.current = 'Edit Lists'


class EditorText(TextInput):
    def update_item(self, *args):
        gen = Generator()
        items = self.text.strip().split('\n')
        items.sort()
        items = set(items)
        gen.lst[self.id] = list(filter(None, items))
        gen.export_lst()


class EditListsScreen(Screen):
    @mainthread
    def on_enter(self):
        gen = Generator()
        edit_grid = GridLayout()
        edit_grid.cols = 4
        edit_grid.rows = 4
        edit_grid.padding = 10
        for key in gen.lst:
            box = BoxLayout()
            box.orientation = 'vertical'
            box.padding = 10

            label = Label()
            label.text = key
            label.size_hint = (1, .25)

            text_input = EditorText()
            text_input.multiline = True
            text_input.text = self.get_values(gen.lst[key])
            text_input.id = key

            button = Button(text='Submit')
            button.size_hint = (1, .25)
            button.bind(on_press=text_input.update_item)

            box.add_widget(label)
            box.add_widget(text_input)
            box.add_widget(button)
            edit_grid.add_widget(box)

        button = Button()
        button.text = 'Done'
        button.size_hint = (1, .25)
        button.bind(on_press=self.load_art_tools_main)
        edit_grid.add_widget(button)
        self.add_widget(edit_grid)

    def get_values(self, the_list):
        value = ''
        for item in the_list:
            value += f'{item}\n'
        return value

    def load_art_tools_main(self, *args):
        for child in self.children:
            self.remove_widget(self.children[-1])
        self.manager.current = "Kyle's Art Tools"


class ArtToolsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ArtToolsScreen())
        sm.add_widget(PictureViewerScreen())
        sm.add_widget(EditListsScreen())
        return sm


if __name__ == '__main__':
    ArtToolsApp().run()
