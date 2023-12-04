from ui.ui import Ui
from repositories.reference_writer import ReferenceWriter
from services.console_io import ConsoleIO


def main():
    reference_writer = ReferenceWriter()
    io = ConsoleIO()
    ui = Ui(reference_writer, io)
    ui.run()

if __name__ == "__main__":
    main()
