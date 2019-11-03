from practice.generate_pic import FigureDrawing
from practice.user_messenger import UserMessenger
from practice.exercise_generator import Exercise
from practice.study_generator import Study


def launch_practice_tool():
    msg = UserMessenger()
    another_tool = msg.YES
    while another_tool == msg.YES:
        tool_selected = msg.tool_selection()

        if tool_selected == msg.FIGURE_DRAWING:
            with open('path.txt', "r") as paths_file:
                file_array = paths_file.readlines()
                fig = FigureDrawing(file_array[0])
                fig.generate_pic()

        elif tool_selected == msg.EXERCISE:
            exercise = Exercise()
            exercise.generate()

        elif tool_selected == msg.STUDY:
            study = Study()
            study.generate()

        else:
            msg.closing_software()

        another_tool = msg.another_tool()
