from lib.messenger import Messenger


class UserMessenger(Messenger):
    EDIT_LIST = 'q'
    ITEM_GENERATOR = 'i'
    CHARACTER_GENERATOR = 'c'
    ENVIRONMENT_GENERATOR = 'e'
    GENERATE_ALL = 'a'

    def tool_selection(self):
        print("\n\n",
              "Welcome to Kyle's Draw tools.",
              f"\n\t({UserMessenger.ENVIRONMENT_GENERATOR} + ENTER) -- Environment Generator",
              f"\n\t({UserMessenger.ITEM_GENERATOR} + ENTER) -- Item Generator",
              f"\n\t({UserMessenger.CHARACTER_GENERATOR} + ENTER) -- Character Generator",
              f"\n\t({UserMessenger.GENERATE_ALL} + ENTER) -- Generate all",
              f"\n\t({UserMessenger.EDIT_LIST} + ENTER) -- Edit Lists",
              "\n\t(any other key) -- Exit")
        return UserMessenger.what_todo()
