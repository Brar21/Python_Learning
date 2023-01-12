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