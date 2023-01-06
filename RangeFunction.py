#Range function in Python
#first example you see in  "Loops.py" file and why it start from zero you may learn there
# if you want to start from you choice number than can do like this:

for i in range(5,11):
        print(i)
# in this example number start printing from 5 and print till 10 means in between 5 to 11
#  5 is starting point and upto 11 meas "11" is edn point
# Now how you can skip numbers between than
# Note you can set after first print how many number you want to skip every time#
# Example is shown below
for i in range(1,10,2):
    print(i) # after print number two number you skipping in this example

#print table take "input" from user

value=int(input("Enter number \n"))#user input dega table print krne k liye
for i in range(1,11):
    print(str(value)+"x"+str(i)+"="+str(i*value))
    # print with f strings
    print(f"{value}X{i}={value*1}") #cool method to print table

# to find out string start with letter 'S'
l1=["Sonia","simran","Kunal","Manpreet","SUkhi","Jalandher"]
#count=0
for i in l1:
    if i.startswith("S" ):

        print("Hello"+ i) 
           
# For loop with else condition 
# when if condition done his work it will print

for i in range(12):
    print(i)
else: # this is known as optional "Else" your choice you want to use or not
    print("after done for loop condtion do this "+str(i+1))         

# Break statement to stop loop in between when given conditon is true:
# example:
#for i in range(18):
#    print(i)
#    if i==2: #here when i value become 2 like i==2 than loop will stop there
#        break    #you check this with run in trminal.

# you can use rangeFunction in Break statement also
#example:
for i in range (2,18,2): 
    print(i)
    if i==6: # we see on only three number are print
      break   


#Continue statement use case Example to better understanding:
# 
for i in range(2,12):
    if i%2==0: # hume yha pe keh rhe hai if "i" "index" number is even than not print that value
        continue
    print(i)    #means we are printing only "Odd" indexs here


#Continue statement use case Example to better understanding:
# 
#result=32 #number 32 to result hojayega "Fail" or pitaayi pkki hogi aapki
result=35 #number 33 ya isse jyada ho to apko koi jwaab nai milega
if result>=33:
    pass # bs mujhe kuch nai krna 33 agye mere main pass hogya bs
else: 
    print("Fail ho aap bhai")



#exercise for understand
# Pattrn print
#
# #
# # #

n=3
for i in range(4):
    print("*"*(i+1))    #this is way to this


#pattran     *
#           * *
#        * * * * *    

n=5
for i in range(5):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(n-i-1))

n=5
for i in range(5):    # *
    print(" "*(1-i-n))# **
    print("*"*(1+i*3))# ***
#print(" "*(1-i-n))   # ****