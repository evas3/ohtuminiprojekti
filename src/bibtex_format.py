import re

file_path = 'src/data/references.bib'

class Bibtex:
    def __init__(self):
        pass

    def key_from_bib_entry(self, entry):
        match = re.search(r'@\w+\{(.*?),', entry)
        if match:
            return match.group(1)
        return None

    def key(self, author, year):
        new_key = f"{author}{year}" if len(author) <= 3 else f"{author[:3]}{year}"

        try:
            with open(file_path, 'r') as file:
                content = file.read() 
                entries = re.split(r'(?=@\w+{)', content)[1:]
                existing_keys = {self.key_from_bib_entry(entry) for entry in entries}
        except FileNotFoundError:
            print(f"File {file_path} not found.")

        count = 0
        orginal_key = new_key
        while new_key in existing_keys:
            suffix = chr(ord('A') + count)
            new_key = f"{orginal_key}{suffix}"
            count += 1

        return new_key

    def book(self, title, author, year, publisher, address):
        refrence = """
@Book{"""+self.key(author, year)+""",
  author    = {"""+str(author)+"""},
  title     = {"""+str(title)+"""},
  publisher = {"""+str(publisher)+"""},
  year      = {"""+str(year)+"""},
  address   = {"""+str(address)+"""}
}"""
        return refrence

    def article(self, author, title, journal, year, volume, pages):
        refrence = """
@article{"""+self.key(author, year)+""",
  author  = {"""+str(author)+"""},
  title   = {"""+str(title)+"""},
  journal = {"""+str(journal)+"""},
  year    = {"""+str(year)+"""},
  volume  = {"""+str(volume)+"""},
  pages   = {"""+str(pages)+"""}
}"""
        return refrence

    def inproceedings(self, author, title, booktitle, year):
        refrence = """
@inproceedings{"""+self.key(author, year)+""",
  author    = {"""+str(author)+"""},
  title     = {"""+str(title)+"""},
  booktitle = {"""+str(booktitle)+"""},
  year      = {"""+str(year)+"""},
}"""
        return refrence
