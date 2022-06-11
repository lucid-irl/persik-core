class Animal():
    def __init__(self) -> None:
        print("Animal Create!")
        
    def whoAmI(self) -> None:
        print("Animal")
        
    def eating(self):
        print("Eating")

class Dog(Animal):
    def __init__(self) -> None:
        print("Dog Create!")
        
    def bark(self):
        print("Gau gau")

# mya = Animal()
# mya.eating()

# mydog = Dog()
# mydog.eating()
# mydog.bark()
        
class Book():
    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self) -> str:
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)
        
    def __len__(self)-> int:
        return self.pages
    
    def __del__(self) -> None:
        return print("Deleted")
    
mybook = Book("Python", "Hoang", 195)
print(mybook.title)
print(len(mybook))
del mybook
print(mybook)
