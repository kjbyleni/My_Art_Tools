import os

from .character_generator import CharacterGenerator
from .item_generator import ItemGenerator
from .env_generator import EnvironmentGenerator
from lib.generator import Generator

EDIT_LIST = 'q'
ITEM_GENERATOR = 'i'
CHARACTER_GENERATOR = 'c'
ENVIRONMENT_GENERATOR = 'e'
GENERATE_ALL = 'a'
YES = 'y'


def print_items(items):
    for item in items:
        print(f'\t\t{item}')


def print_result(items, context):
    print(
        '\n\t',
        f'---------   Creating your {context}  ---------'
    )
    print_items(items)
    print(f'\t -----------   {context} Created!   -----------\n')


def validate_is_number(how_many=None, attempt=0):
        if how_many is None:
            how_many = input('How Many? ')
        try:
            return int(how_many)
        except ValueError:
            print("input must be a number")
            if attempt > 1:
                print("too many attempts!")
            else:
                validate_is_number(how_many=None, attempt=attempt + 1)


def launch_draw_tool():
    print("\n\n",
          "Welcome to Kyle's Draw tools.",
          f"\n\t({ENVIRONMENT_GENERATOR} + ENTER) -- Environment Generator",
          f"\n\t({ITEM_GENERATOR} + ENTER) -- Item Generator",
          f"\n\t({CHARACTER_GENERATOR} + ENTER) -- Character Generator",
          f"\n\t({GENERATE_ALL} + ENTER) -- Generate all",
          f"\n\t({EDIT_LIST} + ENTER) -- Edit Lists",
          "\n\t(any other key) -- Exit")

    another_tool = YES
    while another_tool == YES:
        tool_selected = input("Which Tool? ")

        if tool_selected == ENVIRONMENT_GENERATOR:
            EnvironmentGenerator().generate()

        elif tool_selected == ITEM_GENERATOR:
            how_many = validate_is_number()
            ItemGenerator().generate_multiple(how_many)

        elif tool_selected == CHARACTER_GENERATOR:
            CharacterGenerator().generate()

        elif tool_selected == GENERATE_ALL:
            EnvironmentGenerator().generate()
            CharacterGenerator().generate()
            ItemGenerator().generate_multiple(4)

        elif tool_selected == EDIT_LIST:
            generator = Generator()
            # print keys
            print_items(generator.get_keys())
            key = input("\nWhich list to modify? ")
            f = open(generator.temp_path, 'w')
            if key in generator.lst:
                for item in sorted(generator.lst[key]):
                    # print existing list
                    f.write(f'{item}\n')
                f.close()

                # open notepad.exe allow user to edit.  Wait until done editing
                os.system(f'notepad.exe {generator.temp_path}')
                generator.lst[key] = generator.convert_file_to_array(generator.temp_path)
                generator.export_lst()
                if os.path.exists(generator.temp_path):
                    os.remove(generator.temp_path)
                    print("SUCCESS!")

        else:
            print('Closing software')
            exit()

        print("Good Luck!")
        another_tool = input("would you like another tool? (y,n)")
