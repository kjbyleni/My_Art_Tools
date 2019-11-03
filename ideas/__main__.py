from .character_generator import CharacterGenerator
from .item_generator import ItemGenerator
from .env_generator import EnvironmentGenerator
from lib.generator import Generator
from ideas.user_messenger import UserMessenger


def launch_draw_tool():
    msg = UserMessenger()
    another_tool = msg.YES
    while another_tool == msg.YES:
        env = EnvironmentGenerator()
        character = CharacterGenerator()
        drawing_items = ItemGenerator()
        tool_selected = msg.tool_selection()

        if tool_selected == msg.ENVIRONMENT_GENERATOR:
            env.generate()

        elif tool_selected == msg.ITEM_GENERATOR:
            drawing_items.generate()

        elif tool_selected == msg.EDIT_LIST:
            generator = Generator()
            msg.print_items(generator.get_keys())
            lst_to_modify = msg.which_list()
            generator.edit_lst(lst_to_modify)

        elif tool_selected == msg.CHARACTER_GENERATOR:
            character.generate()

        elif tool_selected == msg.GENERATE_ALL:
            env.generate()
            character.generate()
            drawing_items.generate(4)
        else:
            msg.closing_software()

        msg.good_luck()
        another_tool = msg.another_tool()
