
#num=int(input())

class Calculater:

    def __init__(self,num):
        self.number=num

        def sequare(self):
            print(f"Sequare of {self.number} is {self.number**2}")

        def sequareRoot(self):
            print(f"SequareRoot of {self.number} is {self.number**2}")

        def cube(self):
            print(f"Cube of {self.number} is {self.number**0.5}")        

a=Calculater(5)
a.sequare()
a.sequareRoot()
a.cube()        

