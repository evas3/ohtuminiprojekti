
class ReferenceWriter:
    def __init__(self):
        pass

    def write(self, data):
        with open('references.bib', 'a', encoding="utf-8") as f:
            f.write(data)