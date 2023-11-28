import os
from settings import DIRNAME

class ReferenceWriter:
    def __init__(self):
        self.filename = "references.bib"
        self.data_file_path = ""

    def new_filename(self, filename):
        self.filename = filename

    def write(self, data):
        self.data_file_path = os.path.join(DIRNAME, "data", self.filename)
        try:
            with open(self.data_file_path, 'a', encoding="utf-8") as f:
                f.write(data)
            return True
        except UnicodeEncodeError:
            return False
