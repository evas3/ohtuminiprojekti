from bibtex_format import Bibtex

class Ui:
    def __init__(self, reference_writer, io):
        self.reference_writer = reference_writer
        self.io = io

        self.commands = {
            0: self.show_commands,
            1: self.add_book_citation,
            2: self.add_article_citation,
            3: self.add_inproceedings_citation,
            4: self.create_new_file,
            9: self.exit_app,
                        }
        self.loop = True

    def show_commands(self):
        self.io.write("0: Show all available operation commands")
        self.io.write("1: Add book citation")
        self.io.write("2: Add article citation")
        self.io.write("3: Add inproceedings citation")
        self.io.write("4: Create new BibTex file")
        self.io.write("9: Exit application")

    def add_book_citation(self):
        self.io.write("Please add the following information")

        title = self.io.read("   Add title: ")
        author = self.io.read("   Add author: ")
        year = self.io.read("   Add year: ")
        publisher = self.io.read("   Add publisher: ")
        address = self.io.read("   Add address: ")

        citation = Bibtex().book(title, author, year, publisher, address)
        if self.reference_writer.write(citation):
            self.io.write("Book citation added succesfully")
        else:
            self.io.write("Citation could not be added")
        self.loop = True

    def add_article_citation(self):
        self.io.write("Please add the following information")

        title = self.io.read("   Add title: ")
        author = self.io.read("   Add author: ")
        year = self.io.read("   Add year: ")
        journal = self.io.read("   Add journal: ")
        volume = self.io.read("   Add volume: ")
        pages = self.io.read("   Add pages: ")

        citation = Bibtex().article(author, title, journal, year, volume, pages)
        if self.reference_writer.write(citation):
            self.io.write("Article citation added succesfully")
        else:
            self.io.write("Citation could not be added")
        self.loop = True

    def add_inproceedings_citation(self):
        self.io.write("Please add the following information")

        title = self.io.read("   Add title: ")
        author = self.io.read("   Add author: ")
        year = self.io.read("   Add year: ")
        booktitle = self.io.read("   Add booktitle: ")

        citation = Bibtex().inproceedings(author, title, booktitle, year)
        if self.reference_writer.write(citation):
            self.io.write("Article citation added succesfully")
        else:
            self.io.write("Citation could not be added")
        self.loop = True

    def exit_loop(self):
        self.loop = False

    def run(self):
        self.menu()

        while self.loop:
            self.io.write("")
            command = self.io.read("""
    Select the operation you want to perform (enter 0 to show all): 
                """)
            try:
                operation = int(command)
                if operation in self.commands:
                    self.commands[operation]()
                else:
                    self.io.write("Invalid, please try again with correct command")
            except ValueError:
                self.io.write("Please enter a valid number")

    def menu(self):
        self.io.write("Welcome to the app!")
        self.io.write("")
        self.io.write("Available commands")
        self.show_commands()

    def exit_app(self):
        raise SystemExit

    def create_new_file(self):
        new_filename = self.io.read("Please enter a new filename:")
        self.reference_writer.new_filename(new_filename)
