
class Bibtex:
    def __init__(self):
        pass

    def key(self, author, year):
        if len(author) <= 3:
            return str(author)+str(year)
        else:
            return str(author[:3])+str(year)
        
    def book(self, key, title, author, year, publisher, address):
        refrence = """
@Book{"""+key+""",
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
    
    def iproceedings(self, author, title, booktitle, year):
        refrence = """
@inproceedings{"""+self.key(author, year)+""",
    author    = {"""+str(author)+"""},
    title     = {"""+str(title)+"""},
    booktitle = {"""+str(booktitle)+"""},
    year      = {"""+str(year)+"""},
}
"""
        return refrence