
class ValidateParameters:

    def validate_parameters_book(self, title, author, year, publisher, address):
        str_inputs = title, author, publisher, address

        if any(not s or any(char.isnumeric() for char in s) for s in str_inputs):
            return False
        if not year or not year.isnumeric() or len(year)>4 or len(year) <=0:
            return False
        return True

    def validate_parameters_article(self, title, author, year, journal, volume):
        str_inputs = title, author, journal
        int_inputs = volume, year

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
    