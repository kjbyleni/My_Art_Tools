from practice import __main__ as practice_tool
from ideas import __main__ as draw_tool
from lib.messenger import Messenger


def main():
    msg = Messenger()
    tool_selected = msg.tool_selection()

    if tool_selected == msg.DRAW:
        draw_tool.launch_draw_tool()

    elif tool_selected == msg.PRACTICE:
        practice_tool.launch_practice_tool()

    else:
        msg.closing_software()


if __name__ == '__main__':
    main()
