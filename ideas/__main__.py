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
        env = EnvironmentGenerator()
        character = CharacterGenerator()
        drawing_items = ItemGenerator()
        tool_selected = input("Which Tool? ")

        if tool_selected == ENVIRONMENT_GENERATOR:
            env.generate()

        elif tool_selected == ITEM_GENERATOR:
            drawing_items.generate()

        elif tool_selected == EDIT_LIST:
            generator = Generator()
            print_items(generator.get_keys())
            lst_to_modify = input("\nWhich list to modify? ")
            generator.edit_lst(lst_to_modify)

        elif tool_selected == CHARACTER_GENERATOR:
            character.generate()

        elif tool_selected == GENERATE_ALL:
            env.generate()
            character.generate()
            drawing_items.generate(4)
        else:
            print('Closing software')
            exit()

        print("Good Luck!")
        another_tool = input("would you like another tool? (y,n)")
