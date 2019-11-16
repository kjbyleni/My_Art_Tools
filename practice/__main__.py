from practice.exercise_generator import Exercise
from practice.generate_pic import FigureDrawing
from practice.study_generator import Study

FIGURE_DRAWING = 'f'
EXERCISE = 'e'
STUDY = 's'
YES = 'y'


def launch_practice_tool():
    print("\n\n",
          "Welcome to Kyle's Practice tools.",
          "\n\t(f + ENTER) -- Figure Drawing",
          "\n\t(e + ENTER) -- Exercise",
          "\n\t(s + ENTER) -- Study",
          "\n\t(any other key) -- Exit")

    another_tool = YES
    while another_tool == YES:
        tool_selected = input("Which Tool? ")

        if tool_selected == FIGURE_DRAWING:
            with open('path.txt', "r") as paths_file:
                file_array = paths_file.readlines()
                fig = FigureDrawing(file_array[0])
                fig.generate_pic()

        elif tool_selected == EXERCISE:
            exercise = Exercise()
            exercise.generate()

        elif tool_selected == STUDY:
            study = Study()
            study.generate()

        else:
            print('Closing software')
            exit()

        another_tool = input("would you like another tool? (y,n)")
