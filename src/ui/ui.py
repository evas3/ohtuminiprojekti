from bibtex_format import Bibtex
from reference_validator import ValidateParameters
from services.bibtex_filter import BibtexFilter
from delete_reference import DeleteReference

class Ui:
    def __init__(self, reference_writer, io):
        self.reference_writer = reference_writer
        self.io = io
        self._running = True

        self.commands = {
            0: self.show_commands,
            1: self.add_book_citation,
            2: self.add_article_citation,
            3: self.add_inproceedings_citation,
            4: self.create_new_file,
            5: self.summarize_written_citations,
            6: self.filter_by,
            7: self.delete_reference,
            8: self.exit_app,
                        }

    def show_commands(self):
        self.io.write("0: Show all available operation commands")
        self.io.write("1: Add book citation")
        self.io.write("2: Add article citation")
        self.io.write("3: Add inproceedings citation")
        self.io.write("4: Create new BibTex file")
        self.io.write("5: Summarize written citations")
        self.io.write("6: Search references")
        self.io.write("7: Delete a reference")
        self.io.write("8: Exit application\n")

    def add_book_citation(self):
        self.io.write("Please add the following information for book citation")

        title = self.io.read("   Add title: ")
        while True:
            author = self.io.read("   Add author: ")
            if not ValidateParameters().validate_parameters_author(author):
                self.io.write("\nauthor must be letters and year max 4 numbers, continue:\n")
                continue
            while True:
                year = self.io.read("   Add year: ")
                if not ValidateParameters().validate_parameters_year(year):
                    self.io.write("\nauthor must be letters and year max 4 numbers, continue:\n")
                    continue
                break
            publisher = self.io.read("   Add publisher: ")
            address = self.io.read("   Add address: ")

            citation = Bibtex().book(title, author, year, publisher, address)
            self.call_writer(citation, "Book", author, year)
            break

    def add_article_citation(self):
        self.io.write("Please add the following information for article citation")

        title = self.io.read("   Add title: ")
        while True:
            author = self.io.read("   Add author: ")
            if not ValidateParameters().validate_parameters_author(author):
                self.io.write("\nauthor must be letters and year max 4 numbers, continue:\n")
                continue
            while True:
                year = self.io.read("   Add year: ")
                if not ValidateParameters().validate_parameters_year(year):
                    self.io.write("\nauthor must be letters and year max 4 numbers, continue:\n")
                    continue
                break
            journal = self.io.read("   Add journal: ")
            volume = self.io.read("   Add volume: ")
            pages = self.io.read("   Add pages: ")

            citation = Bibtex().article(author, title, journal, year, volume, pages)
            self.call_writer(citation, "Article", author, year)
            break

    def add_inproceedings_citation(self):
        self.io.write("Please add the following information for inproceedings citation")

        title = self.io.read("   Add title: ")
        while True:
            author = self.io.read("   Add author: ")
            if not ValidateParameters().validate_parameters_author(author):
                self.io.write("\nauthor must be letters and year max 4 numbers, continue:\n")
                continue
            while True:
                year = self.io.read("   Add year: ")
                if not ValidateParameters().validate_parameters_year(year):
                    self.io.write("\nauthor must be letters and year max 4 numbers, continue:\n")
                    continue
                break
            booktitle = self.io.read("   Add booktitle: ")

            citation = Bibtex().inproceedings(author, title, booktitle, year)
            self.call_writer(citation, "Inproceedings", author, year)
            break

    def call_writer(self, citation, citation_type, author, year):
        success_text = f"\n{citation_type} citation added succesfully!\n"
        if self.reference_writer.write(citation) and self.reference_writer.write_shortform(
            citation_type, author, year):
            self.io.write(success_text)
        else:
            self.io.write("\nCitation could not be added, try again!\n")

    def run(self):
        self.menu()

        while self._running:
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
        self._running = False

    def create_new_file(self):
        new_filename = self.io.read("Please enter a new filename: ")
        self.reference_writer.new_filename(new_filename)
        self.io.write(f'\nNew file with a name {new_filename} created\n')

    def summarize_written_citations(self):
        citations = self.reference_writer.summarize()
        self.io.write("Here are the written citations by key, type, author, year:\n")
        for citation in citations:
            self.io.write(citation)

    def filter_by(self):
        filter_type = self.io.read("Search by (citation type, i.e. author or year): ")
        keyword = self.io.read("Keyword (i.e author's name or year): ")
        self.io.write("Search results: \n")
        self.filter_by_arguments(filter_type, keyword)

    def delete_reference(self):
        key = self.io.read("Key for reference you want to delete: ")
        references = self.reference_writer.read_file()
        file = self.reference_writer.current_file_path()
        row_index_and_number = DeleteReference().key_check(str(key), references)
        print(row_index_and_number)
        if row_index_and_number[1] > -1:
            confirmation = self.io.read(f"Press 'y' to delete reference with key {key}: ")
            if confirmation == "y":
                index = row_index_and_number[0]
                number = row_index_and_number[1]
                if DeleteReference().delete_reference(file, index, number):
                    self.io.write("\nReference deleted\n")
                else:
                    self.io.write("\nFailed to delete\n")
        else:
            self.io.write("\nKey not found\n")

    def filter_by_arguments(self, filter_type, keyword):
        all_references = self.reference_writer.read_file()
        filtered_references = BibtexFilter().filter_by(filter_type, keyword, all_references)
        for result in filtered_references:
            for row in result:
                self.io.write(row)
