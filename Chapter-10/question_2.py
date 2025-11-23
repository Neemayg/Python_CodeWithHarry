class Book:
  def __init__(self,title,author,price):
    self.title=title
    self.author=author
    self.price=price

  def values(self):
    print("-----Book Details------")
    print(f"{self.title} is tile")
    print(f"{self.author} is author")
    print(f"{self.price:.2f} is price")

book1=Book("Atomic Habits","Neemay",127)
book1.values()
    