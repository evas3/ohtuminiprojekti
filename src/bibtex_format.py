

def book(key, title, author, year, publisher, address):
    refrence = """
@Book{"""+str(key)+""",
  author    = """+str(author)+""",
  title     = """+str(title)+""",
  publisher = """+str(publisher)+""",
  year      = """+str(year)+"""
}"""
    return refrence
