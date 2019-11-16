from practice.generate_pic import FigureDrawing

import practice.factory as practice_factory
import lib.utils as utils

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
          "\n\t(any other key) -- Exit")
    return input('Which tool? ')


def launch_practice_tool():

    options = [FIGURE_DRAWING, EXERCISE, STUDY]
    tool_selected = welcome()

    while tool_selected in options:
        welcome()

        if tool_selected == FIGURE_DRAWING:
            with open('path.txt', "r") as paths_file:
                file_array = paths_file.readlines()
                fig = FigureDrawing(file_array[0])
                how_many = utils.validate_is_number()
                fig.generate_pic(how_many)

        elif tool_selected == EXERCISE:
            practice_factory.get_exercise().generate()

        elif tool_selected == STUDY:
            practice_factory.get_study().generate()

        else:
            print('Closing software')
            exit()

        tool_selected = welcome()


if __name__ == '__main__':
    launch_practice_tool()
