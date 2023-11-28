from bibtex_format import Bibtex
from repositories.reference_writer import ReferenceWriter

class Ui:
    def __init__(self):

        self.commands = {
            0: self.show_commands,
            1: self.add_book_citation,
            9: self.exit_app,
                        }
        self.loop = True

    def show_commands(self):
        print("0: Show all available operation commands")
        print("1: Add book citation")
        print("9: Exit application")

    def add_book_citation(self):
        print("Please add the following information")
        key = input("Add key (enter 'q' to exit): ")
        if key.lower() == 'q':
            return
        title = input("Add title: ")
        author = input("Add author: ")
        year = input("Add year: ")
        publisher = input("Add publisher: ")
        address = input("Add address: ")

        reference_writer = ReferenceWriter()
        citation = Bibtex.book(key, title, author, year, publisher, address)
        reference_writer.write(citation)

        print("book citation added succesfully")
        self.loop = True

    def exit_loop(self):
        self.loop = False

    def run(self):
        self.menu()

        while self.loop:
            print("")
            command = input("Select the operation you want to perform (enter 0 to show all): ")
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

    def exit_app(self):
        raise SystemExit
