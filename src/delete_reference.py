

class DeleteReference:

    def key_check(self, key, references):
        row_index = -1
        row_number = -1
        for reference in references:
            for row in reference:
                row_index += 1
                if key in row:
                    row_number = len(reference)
                    return [row_index, row_number]
        return [row_index, row_number]

    def delete_reference(self, file, row_index, row_number):
        try:
            with open(file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            with open(file, "w", encoding="utf-8") as ref_file:
                for number, line in enumerate(lines):
                    if number not in range(row_index, row_index+row_number):
                        if line != "":
                            ref_file.write(line)
            return True

        except FileNotFoundError:
            return False

    def delete_shortform(self, file, key):
        try:
            with open(file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            num = -1
            for num, line in enumerate(lines):
                if key in line:
                    row = num
                    break
            with open(file, "w", encoding="utf-8") as ref_file:
                for num, line in enumerate(lines):
                    if num != row and line != "":
                        ref_file.write(line)
            return True

        except FileNotFoundError:
            return False
