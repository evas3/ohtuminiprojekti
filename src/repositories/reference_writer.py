
class ReferenceWriter:
    def __init__(self):
        self.reference = ""

    def write(self, type, data):
        self.reference += f"@{type}" + "{" + data
        with open('references.bib', 'w') as f:
            f.write(self.reference)

