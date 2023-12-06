from bibtex_format import Bibtex

class Ui:
    def __init__(self, reference_writer, io):
        self.reference_writer = reference_writer
        self.io = io
        self._runnning = True

        self.commands = {
            0: self.show_commands,
            1: self.add_book_citation,
            2: self.add_article_citation,
            3: self.add_inproceedings_citation,
            4: self.create_new_file,
            5: self.summarize_written_citations,
            9: self.exit_app,
                        }

    def show_commands(self):
        self.io.write("0: Show all available operation commands")
        self.io.write("1: Add book citation")
        self.io.write("2: Add article citation")
        self.io.write("3: Add inproceedings citation")
        self.io.write("4: Create new BibTex file")
        self.io.write("5: Summarize written citations")
        self.io.write("9: Exit application\n")

    def validate_parameters_book(self, title, author, year, publisher, address):
        str_inputs = title, author, publisher, address

        if any(not s or any(char.isnumeric() for char in s) for s in str_inputs):
            return False
        if not year or not year.isnumeric() or len(year)>4 or len(year) <=0:
            return False
        return True

    def validate_parameters_article(self, title, author, year, journal, volume, pages):
        str_inputs = title, author, journal
        int_inputs = volume, pages, year

        if any(not s or any(char.isnumeric() for char in s) for s in str_inputs):
            return False
        if any(not str(i).isnumeric() for i in int_inputs) or len(year)>4 or len(year) <=0:
            return False
        return True

    def validate_parameters_inproceedings(self, title, author, year, booktitle):
        str_inputs = title, author, booktitle

        if any(not s or any(char.isnumeric() for char in s) for s in str_inputs):
            return False
        if not year or not year.isnumeric() or len(year)>4 or len(year) <=0:
            return False
        return True

    def add_book_citation(self):
        self.io.write("Please add the following information for book citation")

        title = self.io.read("   Add title: ")
        author = self.io.read("   Add author: ")
        year = self.io.read("   Add year: ")
        publisher = self.io.read("   Add publisher: ")
        address = self.io.read("   Add address: ")

        if not self.validate_parameters_book(title, author, year, publisher, address):
            self.io.write("\nCould not validate the inputs, use alphabets and numbers correctly!\n")
            return

        citation = Bibtex().book(title, author, year, publisher, address)
        self.call_writer(citation, "Book", author, year)

    def add_article_citation(self):
        self.io.write("Please add the following information for article citation")

        title = self.io.read("   Add title: ")
        author = self.io.read("   Add author: ")
        year = self.io.read("   Add year: ")
        journal = self.io.read("   Add journal: ")
        volume = self.io.read("   Add volume: ")
        pages = self.io.read("   Add pages: ")

        if not self.validate_parameters_article(title, author, year, journal, volume, pages):
            self.io.write("\nCould not validate the inputs, use alphabets and numbers correctly!\n")
            return

        citation = Bibtex().article(author, title, journal, year, volume, pages)
        self.call_writer(citation, "Article", author, year)

    def add_inproceedings_citation(self):
        self.io.write("Please add the following information for inproceedings citation")

        title = self.io.read("   Add title: ")
        author = self.io.read("   Add author: ")
        year = self.io.read("   Add year: ")
        booktitle = self.io.read("   Add booktitle: ")

        if not self.validate_parameters_inproceedings(title, author, year, booktitle):
            self.io.write("\nCould not validate the inputs, use alphabets and numbers correctly!\n")
            return

        citation = Bibtex().inproceedings(author, title, booktitle, year)
        self.call_writer(citation, "Inproceedings", author, year)

    def call_writer(self, citation, citation_type, author, year):
        success_text = f"\n{citation_type} citation added succesfully!\n"
        if self.reference_writer.write(citation):
            self.reference_writer.write_shortform(citation_type, author, year)
            self.io.write(success_text)
        else:
            self.io.write("\nCitation could not be added, try again!\n")

    def run(self):
        self.menu()

        while self._runnning:
            command = self.io.read("   Select the operation you want to perform (0 to show all): ")
            self.io.write("")
            try:
                operation = int(command)
                if operation in self.commands:
                    self.commands[operation]()
                else:
                    self.io.write("\nInvalid, please try again with correct command\n")
            except ValueError:
                self.io.write("\nPlease enter a valid number\n")

    def menu(self):
        self.io.write("Welcome to the app!\n")
        self.io.write("Available commands")
        self.show_commands()

    def exit_app(self):
        self._runnning = False

    def create_new_file(self):
        new_filename = self.io.read("Please enter a new filename: ")
        self.reference_writer.new_filename(new_filename)
        self.io.write(f'\nNew file with a name {new_filename} created\n')

    def summarize_written_citations(self):
        citations = self.reference_writer.summarize()
        self.io.write("\nHere are the written citations:\n")
        for citation in citations:
            self.io.write(citation)
