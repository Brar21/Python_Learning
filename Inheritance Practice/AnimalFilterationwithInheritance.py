#Multi-level Inheritance
class Animal:
    animalType="mammal"
class Pets:
    color:"white"
    legs:"four"
    tail:"small"
    bread:"Labraydor"
class Dog:
    @staticmethod
    def bark():
        print("Bow Bow!")        

dog=Dog()
dog.bark()