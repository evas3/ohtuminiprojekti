
class ValidateParameters:

    def validate_parameters_book(self, title, author, year, publisher, address):
        str_inputs = [str(title), str(author), str(publisher), str(address)]

        if any(not s or any(char.isnumeric() for char in s) for s in str_inputs):
            return False
        if not (str(year).isnumeric() and 0 < len(str(year)) <= 4):
            return False

        return True

    def validate_parameters_article(self, title, author, year, journal, volume):
        str_inputs = [str(title), str(author), str(journal)]

        if any(not s or any(char.isnumeric() for char in s) for s in str_inputs):
            return False
        if not (str(year).isnumeric() and 0 < len(str(year)) <= 4):
            return False
        if not (str(volume).isnumeric() and str(volume).strip()):
            return False

        return True

    def validate_parameters_inproceedings(self, title, author, year, booktitle):
        str_inputs = [str(title), str(author), str(booktitle)]

        if any(not s or any(char.isnumeric() for char in s) for s in str_inputs):
            return False
        if not (str(year).isnumeric() and 0 < len(str(year)) <= 4):
            return False

        return True
