from ui.ui import Ui
from repositories.reference_writer import ReferenceWriter
from tests.stub_io import StubIO

class AuthenticationError(Exception):
    pass

class AppLibrary:
    def __init__(self):
        self.reference_writer = ReferenceWriter()
        self.io = StubIO()
        self.app = Ui(self.reference_writer, self.io)

    def input(self, value):
        self.io.add_input(value)

    def run_application(self):
        self.app.run()

    def output_should_contain(self, value):
        outputs = self.io.outputs
        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )
