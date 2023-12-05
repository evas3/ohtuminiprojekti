
class ConsoleIO:
    def write(self, output):
        print(output)

    def read(self, value):
        return input(f'{value: <18}').strip()
