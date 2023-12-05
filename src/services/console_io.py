
class ConsoleIO:
    def write(self, output):
        print(output)

    def read(self, value):
        max_value_length = 18
        formatted_value = f'{value: <{max_value_length}}'
        return input(formatted_value).strip()
