from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from practice.picture_viewer_components import PictureViewerScreen
from ideas.ideas_tools_components import ArtToolsScreen


class ArtToolsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ArtToolsScreen())
        sm.add_widget(PictureViewerScreen())
        return sm


if __name__ == '__main__':
    ArtToolsApp().run()
