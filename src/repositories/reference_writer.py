import os
from settings import DIRNAME

class ReferenceWriter:
    def __init__(self):
        self._filename = "references.bib"
        self.data_file_path = ""

    def new_filename(self, filename):
        self._filename = filename + ".bib"

    def write(self, data):
        self.data_file_path = os.path.join(DIRNAME, "data", self._filename)
        try:
            with open(self.data_file_path, 'a', encoding="utf-8") as f:
                f.write(data)
            return True
        except UnicodeEncodeError:
            return False
        
    def read_file(self):
        """ Returns references in a nested list, highest level has a list of
        complete references, and individual lists consist of the lines in a
        single reference"""
        
        try:
            all_lines, single_reference, all_references = [], [], []
            with open(self._filename, "r", encoding="utf-8") as file:
                all_lines = [(line.strip("\n")) for line in file.readlines()]
            for line in all_lines:
                if line == "}":
                    single_reference.append(line)
                    all_references.append(single_reference)
                    single_reference = []
                else:
                    single_reference.append(line)
            return all_references
        except FileNotFoundError:
            return []
