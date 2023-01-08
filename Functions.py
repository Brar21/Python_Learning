
#you want get percentage of student marks
score=[33,56,55,78,98,85]
percent=(sum(score)/600)*100
#print(percent) #you can see we got 67.5% 
#what you will do if you have to find more than 10 students
#you have to write same code every which make you work lengthy

#Example:
#score2
score2=[33,56,55,78,98,85]
percent=(sum(score2)/600)*100
#print(percent)

#score3
score3=[33,56,55,78,98,85]
percent=(sum(score3)/600)*100
#print(percent)

#score4
score4=[33,56,55,78,98,85]
percent=(sum(score4)/600)*100
#print(percent)


#score5
score5=[33,56,55,78,98,85]
percent=(sum(score5)/600)*100
#print(percent) # this will you do every time for all students

#function Example:

def function():
    print("Hello function good morning")

function() #call to function for print ("Hello function good morning") this is importent* step

#you can reduce this code length and you work length also with functions let see Example:
# "def" for write function and than name o funciton:
def percent(score):
    return (sum(score)/600*100)
    
percent=percent(score) #in brackets just chnage value name and you will get all result with this function.
print(percent)    #comement out all upper print to show this functino working

# user name but input() in our function
name=input("Enter Name \n")
def sayHi(name):
    print("Hello good morning " + name)
sayHi(name)


# Default argument which come if you don't provide value than it will print:
Name=input("Enter Name \n")
def sayHii(Name="Viewers"):
    print("Hello good morning " + Name)
sayHii(Name)
sayHii()#while runing this you get "Hello good morning Veiwers" because you not passing any value to it.

