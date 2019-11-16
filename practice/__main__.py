from practice.generate_pic import FigureDrawing

import practice.factory as practice_factory

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


def launch_practice_tool():

    another_tool = YES
    while another_tool == YES:
        welcome()
        tool_selected = input("Which Tool? ")

        if tool_selected == FIGURE_DRAWING:
            with open('path.txt', "r") as paths_file:
                file_array = paths_file.readlines()
                fig = FigureDrawing(file_array[0])
                fig.generate_pic()

        elif tool_selected == EXERCISE:
            practice_factory.get_exercise().generate()

        elif tool_selected == STUDY:
            practice_factory.get_study().generate()

        else:
            print('Closing software')
            exit()

        another_tool = input("would you like another tool? (y,n)")


if __name__ == '__main__':
    launch_practice_tool()
