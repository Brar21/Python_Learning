# with file I/O read file name "myInfo.txt" how?
#let see example

data=open("myInfo.txt",'r') # "r" work as read command for file.
info=data.read()

print(info)
data.close()# here we are asking to computer to after read this file just close thia function