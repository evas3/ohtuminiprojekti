
class Bibtex:
    def __init__(self):
        pass

def book(key, title, author, year, publisher, address):
    refrence = """
@Book{"""+str(key)+""",
  author    = """+str(author)+""",
  title     = """+str(title)+""",
  publisher = """+str(publisher)+""",
  year      = """+str(year)+""",
  address   = """+str(address)+"""
}"""
    return refrence
