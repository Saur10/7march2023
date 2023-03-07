
class  parentAnimal:
    name1="abc"
    name = "adddbc"

    def aa(self):
        print("we are in parent animal class")

class animal(parentAnimal):
    name="rahul"
    def __init__(self):
        print("animal class constructor ")

    def a(self):
        print("i am in animal class")

class mamal(animal):

    def __init__(self):
        print("mamal class constructor ")
    def b(self):
        print("i am in manal class")


ma=mamal()
ma.aa()

print(ma.name)
print(ma.name1)


















