import lib.utils as utils
import practice.factory as practice_factory
from practice.generate_pic import FigureDrawing
from practice.picture_viewer import PictureViewer

EDIT_LIST = 'q'
FIGURE_DRAWING = 'f'
EXERCISE = 'e'
STUDY = 's'
YES = 'y'


def welcome():
    print("\n\n",
          "Welcome to Kyle's Practice tools.",
          "\n\t(f + ENTER) -- Figure Drawing",
          "\n\t(e + ENTER) -- Exercise",
          "\n\t(s + ENTER) -- Study",
          "\n\t(q + ENTER) -- Edit list",
          "\n\t(any other key) -- Exit")
    return input('Which tool? ')


def launch_practice_tool():
    options = [FIGURE_DRAWING, EXERCISE, STUDY, EDIT_LIST]
    tool_selected = welcome()

    while tool_selected in options:
        if tool_selected == FIGURE_DRAWING:
            with open('path.txt', "r") as paths_file:
                file_array = paths_file.readlines()
            PictureViewer.get_instance(file_array[0]).show()

        elif tool_selected == EXERCISE:
            practice_factory.get_exercise().get_rand_image()

        elif tool_selected == STUDY:
            practice_factory.get_study().get_rand_image()

        elif tool_selected == EDIT_LIST:
            utils.edit_file(practice_factory.get_all())

        else:
            print('Closing software')
            exit()

        tool_selected = welcome()


if __name__ == '__main__':
    launch_practice_tool()
