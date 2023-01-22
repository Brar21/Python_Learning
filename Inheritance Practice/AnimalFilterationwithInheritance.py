#Multi-level Inheritance
class Animal:
    animalType="mammal"
class Pets (Animal):
    color="white"
    legs="four"
    tail="small"
    bread="Labraydor"
class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")        

class DogDetails(Pets):
    def DogData(self):
        return self.color
dog=Dog()
dog.bark()
data=DogDetails()
#data.DogData()
print(data.color)