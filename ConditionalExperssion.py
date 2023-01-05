#you will make a decission on base of conditions
#condition full-fill hogi tabi woh am hoga
#other wise say no to work

#Normal example for starting

a=10
if(a>11): #false this condition 10 > 11 because never can be happen
     print("Yes")
elif(a==11):#false this condition 10 = 11 because never can be happen
     print("Equal")
else: #if all of above condition are not pass then this will excute 
    print("No never")

#you can enter as much if and else you want to add. It is call if & else leder.  

#Multiple If conditions

b=1

if(b>1):
    print("Yes")
if(b>0):
    print("b is greater than 0")  #this line will print 
if(b<2):
    print('b is lesser than 2')    #this line will print
if(b==1):
    print("b is equal to 1")    #this line will print
else:
    print("inme se kuch b nai")        


#print true if condition pass or else print false 

year=int(input("Enter date of birthdate \n"))
if year>1995:
    print("True")
else:
    print("False")    

#Relation operators example with conditional experssion

rajuAge=21
if(rajuAge>=21):
    print("Yes") # condition pass than you get "Yes"
else:
    print("No") # condition pass than you get "No"       

# Logiacal operators example

if(rajuAge>20 and rajuAge!=21):
        print("Raju is younger than other")
elif(rajuAge<=21 and rajuAge>=21):
    print("Raju is an adult now")
else:
    print("Raju tu toh abhi bacha hai")            


# let take input from user 
sahrukh=int(input("Enter your age \n"))    

if(sahrukh>20 and sahrukh!=21):
        print("Sahrukh is younger than other")
elif(sahrukh<=21 and sahrukh>=21):
    print("Sahrukh is an adult now")
else:
    print("Sahrukh tu toh abhi bacha hai") 

# IS use

age=21
if age is 21: # Is working here as "==" to check that both value are same or not
    print("You can apply driving license") #if same than it will print this
else :
    print("You can't apply")        