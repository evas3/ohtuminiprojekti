
class StubIO:
    def __init__(self):
        self.inputs = []
        self.outputs = []

    def write(self, output):
        self.outputs.append(output)

    def read(self, value):
        if value:
            return self.inputs.pop(0)
        else:
            return ""
        
    def add_input(self, value):
        self.inputs.append(value)