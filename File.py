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
              
#now use "in" with ".open()" function to check word in present in string or not?
  
with open('mydata.txt','r') as f:
     a=f.read()
     if "now" in a:
        print(True) #we got true because in file "mydata.txt" we have "now" word.
     else:
        print(False)   

#update "gameData.txt" if number you got higher from stored number

def score():
    return 501
get=score()
#first fwe have to read this file
with open('gameData.txt') as f:
    Read=(f.read()) # we have to take as "integer" thats why i use "int"
  
     # what is do if no score is there inside file
if Read=="":
    with open('gameData.txt','w') as f:
        f.write(str(get))
elif int(Read)<get:
    #now we have to write or append in "gameData.txt" if you score is higher only than it can be change
    with open('gameData.txt','w') as f:
        f.write(str(get)) # why str? because ".txt" can only store sting so we have to change result into string
     #now 501 will replace in file with 500
     # but this will happen if newer value is greater than past value.         


## if you want print table file than:
# to make file in differend folder you have to provide folder name first.
for i in range(3,31): #you can create as much table file you want.
    with open(f"table/table of {i}",'w') as f: #table is name of folder adn table is name of file
        for j in range(1, 11):
            f.write(f"{i}x{j}={i*j}\n")     #table files are created in "Table" folder with this simple 4 line code.

# Want to change on particuler word in file

with open("myInfo.txt") as f:
    word=f.read()
word=word.replace("Nabha","Bathinda") # fitst string is for word which you want to rplace with seconf word using ".rplace()" function
#write in file with replacing old word
with open('myInfo.txt','w') as f:
    f.write(word) #word is replace with "Bathinda" new word
# If you want to change more than one word than use "List" with same methhod which show above:

#words=["Varinder singh","Punjab,India","Bathinda"]
#with open("myInfo.txt") as f:
#    word=f.read()
#for i in words:
#    word=word.replace(i,"Varinder Singh Brar")    
#with open('myInfo.txt','w') as f:
#    f.write(word)    #everything change with myname.

#for check word is in file or  not?

with open('myInfo.txt') as f:
    check=f.read()
if "varinder" in check.lower():#after add ".lower()" function in end we can read this
    print("Varinder") #nothing will come but we have word in file in capital-letter so we have to convert this in small-letters.

 ###to check on which line number "varinder is present"   

check=True
i=1
with open('myInfo.txt') as f:
    while check: ##while loop to check full file 
        check=f.readline()#to read line by line
        if "varinder" in check.lower():
            print(i) #it tell right anwer we have "varinder" in 3rd line 
        i+=1     