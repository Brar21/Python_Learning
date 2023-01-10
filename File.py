# with file I/O read file name "myInfo.txt" how?
#let see example

#data=open("myInfo.txt",'r') # "r" work as read command for file.
#one another way to read file 
data=open("myInfo.txt") #like with this  syntan it will take read command by default.
info=data.read()
print(info)
data.close()# here we are asking to computer to after read this file just close thia function

# if you want to read only limted chractors from file

limit=open('myInfo.txt')
prt=limit.read(4) # this will print only "name" word
print(prt) #you got only Four word from file.
limit.close()

# Read only first line ".readline()"
line=open("myInfo.txt")
printLine=line.readline() #this print only first line of file 
print(printLine)
# for sencond line you have to write this function again
printLine=line.readline() #this print only seconed line of file 
print(printLine)
# for third line you have to write this function again
printLine=line.readline() #this print only first line of file 
print(printLine)
line.close()



## Now How to write or create a new file using ".write()" function
letFile= open("mydata.txt",'w') #we have  not any file with "mydata.txt" than it will create this file
Details= letFile.write("Make this file with name mydata")
letFile.close()
  
  # Now add other text in file "mydata.txt" with appending "a" i=use in ".open()" function
Addtext=open('mydata.txt','a')
done= Addtext.write('file is create with this we can add as much as data we want to write in this file using ".open(file_name,"a") than you can append data.')  
Addtext.close()#after this our file is updated you can check in that file.


# It is dificult to remember to close function every time
# you can tackle this with below shown syntax:

with open('mydata.txt','r') as f:
 a=f.read()
 print(a)# now need to close this function
 
#for write file with this syntax:

with open('mydata.txt','a') as f:
         a=f.write("now close function tension finish")
         print(a)
              