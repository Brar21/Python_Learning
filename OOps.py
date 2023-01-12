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
    def info(data):
        print(data.name)
        print(data.place)
        print(data.study)
        print(data.age)
        print(data.bio)
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