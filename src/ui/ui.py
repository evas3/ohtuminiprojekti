class Ui:
    """module to handle the user interface"""
    def __init__(self):

        # Dictionary to handle commands based on their number
        self.commands = {
            0: self.show_commands,
            1: self.add_book_citation,
            9: self.exit_app,
        }

    def show_commands(self):
        print("0: Show all available operation commands")
        print("1: Add book citation")
        print("9: Exit application")

    def add_book_citation(self):
        pass

    def exit_app(self):
        raise SystemExit

    def run(self):
        self.menu()

        while True:
            print("")
            command = input("Select the operation you want to perform (enter 0 to show all): ")
            if command == 9:
                break
            try:
                operation = int(command)
                if operation in self.commands:
                    self.commands[operation]()
                else:
                    print("Invalid, please try again with correct command")
            except ValueError:
                print("Please enter a valid number")

    def menu(self):
        print("Welcome to the app!")
        print("")
        print("Available commands")
        self.show_commands()
