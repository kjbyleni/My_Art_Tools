import os

import ideas.factory as gen_factory
import lib.utils as utils

EDIT_LIST = 'q'
ITEM_GENERATOR = 'i'
CHARACTER_GENERATOR = 'c'
ENVIRONMENT_GENERATOR = 'e'
GENERATE_ALL = 'a'


def welcome():
    print("\n\n",
          "Welcome to Kyle's Draw tools.",
          f"\n\t({ENVIRONMENT_GENERATOR} + ENTER) -- Environment Generator",
          f"\n\t({ITEM_GENERATOR} + ENTER) -- Item Generator",
          f"\n\t({CHARACTER_GENERATOR} + ENTER) -- Character Generator",
          f"\n\t({GENERATE_ALL} + ENTER) -- Generate all",
          f"\n\t({EDIT_LIST} + ENTER) -- Edit Lists",
          "\n\t(any other key) -- Exit")
    return input('Which Tool? ')


def launch_draw_tool():
    options = [EDIT_LIST, ITEM_GENERATOR, CHARACTER_GENERATOR, ENVIRONMENT_GENERATOR, GENERATE_ALL]
    tool_selected = welcome()

    while tool_selected in options:

        if tool_selected == ENVIRONMENT_GENERATOR:
            gen_factory.get_env().get_rand_image()

        elif tool_selected == ITEM_GENERATOR:
            how_many = utils.validate_is_number()
            gen_factory.get_items().generate_multiple(how_many)

        elif tool_selected == CHARACTER_GENERATOR:
            gen_factory.get_character().get_rand_image()

        elif tool_selected == GENERATE_ALL:
            gen_factory.get_all().get_rand_image()

        elif tool_selected == EDIT_LIST:
            utils.edit_file(gen_factory.get_all())

        else:
            print('Closing software')
            exit()

        tool_selected = welcome()


if __name__ == '__main__':
    launch_draw_tool()
