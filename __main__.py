from ideas import __main__ as draw_tool
from practice import __main__ as practice_tool

DRAW = 'd'
PRACTICE = 'p'


def main():
    print("\n\n",
          "Welcome to Kyle's art tools!",
          "\n\t(d + ENTER) -- Draw",
          "\n\t(p + ENTER) -- Practice"
          )

    tool_selected = input("Which Tool? ")

    if tool_selected == DRAW:
        draw_tool.launch_draw_tool()

    elif tool_selected == PRACTICE:
        practice_tool.launch_practice_tool()

    else:
        print('Closing software')
        exit()


if __name__ == '__main__':
    main()
