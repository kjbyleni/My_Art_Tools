from lib.messenger import Messenger


class UserMessenger(Messenger):
    FIGURE_DRAWING = 'f'
    EXERCISE = 'e'
    STUDY = 's'

    def tool_selection(self):
        print("\n\n",
              "Welcome to Kyle's Practice tools.",
              "\n\t(f + ENTER) -- Figure Drawing",
              "\n\t(e + ENTER) -- Exercise",
              "\n\t(s + ENTER) -- Study",
              "\n\t(any other key) -- Exit")
        return UserMessenger.what_todo()

    @staticmethod
    def another_image():
        return input("Would you like another figure? (y,n)")

    @staticmethod
    def print_result_dict(items, context):
        print(
            '\n\t',
            f'---------   Creating your {context}  ---------'
        )
        for key in items:
            print('\n\t',
                  f'{key} -- {items[key]}')
        print(f'\n\t -----------   {context} Created!   -----------\n')
