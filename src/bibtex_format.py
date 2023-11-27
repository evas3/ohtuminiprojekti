
def book(title, author, year, publisher, address):
    refrence = "@book{x,\nauthor = "+author+",\nyear = "+year+",\ntitle = "+title+",\npublisher = "+publisher+",\naddress = "+address+", \n}"
    return refrence

print(book("a", "b", "c", "d", "e"))
