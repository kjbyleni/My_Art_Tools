from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from ideas.edit_components import EditListsScreen
from ideas.ideas_tools_components import ArtToolsScreen
from ideas.picture_viewer_components import PictureViewerScreen


class ArtToolsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ArtToolsScreen())
        sm.add_widget(PictureViewerScreen())
        sm.add_widget(EditListsScreen())
        return sm


if __name__ == '__main__':
    ArtToolsApp().run()
