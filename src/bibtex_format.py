
<<<<<<< HEAD
def book(title, author, year, publisher, address):
    refrence = "@book{x,\nauthor = "+author+",\nyear = "+year+",\ntitle = "+title+",\npublisher = "+publisher+",\naddress = "+address+", \n}"
    return refrence
=======
def book(key, title, author, year, publisher, address):
    refrence = """
    @Book{"""+str(key)+""",
      author    = """+str(author)+""",
      title     = """+str(title)+""",
      publisher = """+str(publisher)+""",
      year      = """+str(year)+"""
    }"""
    return refrence
>>>>>>> cdb5409 (bibtex_format fix)
