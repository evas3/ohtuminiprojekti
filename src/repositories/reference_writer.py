
class ReferenceWriter:
    def __init__(self):
        pass

    def write(self, data):
        with open('references.bib', 'w') as f:
            f.write(data)



