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
            gen_factory.get_env().generate()

        elif tool_selected == ITEM_GENERATOR:
            how_many = utils.validate_is_number()
            gen_factory.get_items().generate_multiple(how_many)

        elif tool_selected == CHARACTER_GENERATOR:
            gen_factory.get_character().generate()

        elif tool_selected == GENERATE_ALL:
            gen_factory.get_all().generate()

        elif tool_selected == EDIT_LIST:
            tmp_path = './tmp_path.json'
            generator = gen_factory.get_all()
            # print keys
            utils.print_items(generator.get_keys())
            key = input("\nWhich list to modify? ")
            f = open(tmp_path, 'w')
            if key in generator.lst:
                for item in sorted(generator.lst[key]):
                    # print existing list
                    f.write(f'{item}\n')
                f.close()

                # open notepad.exe allow user to edit.  Wait until done editing
                os.system(f'notepad.exe {tmp_path}')
                generator.lst[key] = generator.convert_file_to_array(tmp_path)
                generator.export_lst()
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)
                    print("SUCCESS!")

        else:
            print('Closing software')
            exit()

        tool_selected = welcome()


if __name__ == '__main__':
    launch_draw_tool()
