class Messenger:

    def __init__(self):
        pass

    def tool_selection(self):
        print("\n\n",
              "Welcome to Kyle's art tools!",
              "\n\t(d + ENTER) -- Draw",
              "\n\t(p + ENTER) -- Practice"
              )
        return Messenger.what_todo()

    @staticmethod
    def out_of_bounds(lower, upper):
        print(f'Entry must be: {lower} < entry < {upper}')

    @staticmethod
    def good_luck():
        print('Good Luck!')

    @staticmethod
    def what_todo():
        return input("Which Tool? ")

    @staticmethod
    def another_tool():
        return input("would you like another tool? (y,n)")

    @staticmethod
    def how_many():
        return input("\n\nHow many items? ")

    @staticmethod
    def which_list():
        return input("\nWhich list to modify? ")

    @staticmethod
    def input_must_be_number():
        print("Input must be n > 0.  Try again\n\n")

    @staticmethod
    def success():
        print("SUCCESS!")

    @staticmethod
    def too_many_attempts():
        print("Too many attempts.")



    @staticmethod
    def closing_software():
        print("Closing Sofware")
        exit()
