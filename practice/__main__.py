import lib.utils as utils
import practice.factory as practice_factory
from practice.picture_viewer import PictureViewer

FIGURE_DRAWING_INDEX = 0
LANDSCAPE_DRAWING_INDEX = 1

EDIT_LIST = 'q'
FIGURE_DRAWING = 'f'
LANDSCAPE_DRAWING = 'l'
EXERCISE = 'e'
STUDY = 's'
YES = 'y'


def welcome():
    print("\n\n",
          "Welcome to Kyle's Practice tools.",
          "\n\t(f + ENTER) -- Figure Drawing",
          "\n\t(l + ENTER) -- Landscape Drawing",
          "\n\t(e + ENTER) -- Exercise",
          "\n\t(s + ENTER) -- Study",
          "\n\t(q + ENTER) -- Edit list",
          "\n\t(any other key) -- Exit")
    return input('Which tool? ')


def welcome_image_drawing(drawing_type: str):
    print(
        "\n\n",
        f"{drawing_type}. which program would you like?",
        "\n\t(1 + ENTER) -- 5 X 1min, 5 X 2min -- 15 min",
        "\n\t(2 + ENTER) -- 5 X 1min, 5 X 2min, 6 X 5min -- 45min",
        "\n\t(3 + ENTER) -- 5 X 2min, 2 X 5min, 1 X 15min -- 45",
        "\n\t(4 + ENTER) -- 1 X 45min",
        "\n\t(5 + Enter) -- Custom"
    )
    return input("Which tool? ")


def get_program(tool_selected: str):
    if tool_selected == "1":
        return [(1, 5), (2, 5)]
    elif tool_selected == "2":
        return [(1, 5), (2, 5), (6, 5)]
    elif tool_selected == "3":
        return [(2, 5), (5, 2), (15, 1)]
    elif tool_selected == "4":
        return [(45, 1)]
    else:
        time_between = utils.validate_is_number(msg="Time Between Images? ")
        how_many = utils.validate_is_number(msg="How Many Images? ")
        return [(time_between, how_many)]


def stage(path_index, program=[]):
    path = utils.get_path(path_index=path_index)
    picture_viewer = PictureViewer(path)
    picture_viewer.show(program)


def launch_practice_tool():
    options = [FIGURE_DRAWING, LANDSCAPE_DRAWING, EXERCISE, STUDY, EDIT_LIST]
    tool_selected = welcome()

    while tool_selected in options:
        if tool_selected == FIGURE_DRAWING:
            tool_selected = welcome_image_drawing('Figure Drawing')
            picture_viewer = PictureViewer()
            picture_viewer.show(FIGURE_DRAWING_INDEX, get_program(tool_selected))

        elif tool_selected == LANDSCAPE_DRAWING:
            tool_selected = welcome_image_drawing('Landscape Drawing')
            picture_viewer = PictureViewer()
            picture_viewer.show(LANDSCAPE_DRAWING_INDEX, get_program(tool_selected))

        elif tool_selected == EXERCISE:
            practice_factory.get_exercise().generate()

        elif tool_selected == STUDY:
            practice_factory.get_study().generate()

        elif tool_selected == EDIT_LIST:
            utils.edit_file(practice_factory.get_all())

        else:
            print('Closing software')
            exit()

        tool_selected = welcome()


if __name__ == '__main__':
    launch_practice_tool()
