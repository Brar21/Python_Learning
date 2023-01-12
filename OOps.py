#Object oriented programing
#for this we need use of Class

#Example:

class Number:
    def sum(itself):
        return itself.a+itself.b
num=Number()
num.a=20
num.b=30
s=num.sum()        
print(s)

# Example two

#print form 

class DataBase:
    def info(self):
        print(self.name)
        print(self.place)
        print(self.study)
        print(self.age)
        print(self.bio)
yourdata=DataBase()
yourdata.name="Varinder Brar"
yourdata.place="Nabha"
yourdata.study="Human Behaviour"
yourdata.age="28"
yourdata.bio='Simple to understand and tuff for control'       
yourdata.info()



#Example 3:
#if we want change class attribute
class Employee:
            company="Google"     
            salary="100k"

varinder=Employee()
#varinder.salary="75k"  incase these are not presnt than it will show class attribute it in class you can see and you can make ass much you want
#varinder.fullname="Varinder Brar"
#varinder.campany
print(varinder.company)#here compnay is google
Employee.company="Youtube"
print(varinder.company)#now we change this to youtube 
#print(varinder.fullname)
print(varinder.salary)
#if nothing in class or object than it will through an error


#Self parameter
class Employee:
    company="Google"
    def getSalary(self,signature): #it will give parameter automatically
      print(f"salary is {self.salary} \n {signature}") # this is way how self is usefull for

      @staticmethod
      def greets():
        print("Woo! have a party today")

varinder=Employee()
varinder.salary="100k"
varinder.getSalary("Thanks!") #if you not provide parameter self than you have to write as shown below
#varinder.greets()
#Employee.getSalary(varinder)


## like we want to add signature




  # "__init__()" Constructor

class Data:
    info="names"
    def __init__(self):
        print("Name list is ready")

Brar=Data()        
