
class ValidateParameters:
    def validate_parameters(self, author, year):
        if not isinstance(author, str) or not all(char.isalpha() or
        char.isspace() for char in author) or len(author) < 1:
            return False
        if not isinstance(year, str) or not year.isdigit() or len(year) > 4:
            return False

        return True
