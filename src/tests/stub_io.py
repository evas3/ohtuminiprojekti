
class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, output):
        self.outputs.append(output)

    def read(self, value):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return "9"
        
    def add_input(self, value):
        self.inputs.append(value)