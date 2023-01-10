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