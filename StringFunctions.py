#string Functions


#To find full length of String
'''
Find length of string using len(). 
"len" is nothing just short form of length.
'''
example="Find length of string using len()." #space is also counted in length
c= len(example)
print(c)
print(len(example)) # len() and you pass "example" as parameter in function.
# 34 is total length including "spaces".

#to check string last letters are same or not?
'''
To check string endwiths given entry or not
 (it will return true || false)  
'''
myName="varinder"

print(myName.endswith("eer")) #"eer" is value which you will compare with string that it will present in string end or not?
#Answer is "False" because end is "der".Now change "eer" into "der"
print(myName.endswith("der"))
#Answer is "True" this time beacause this is present in string ends.

# To count occurence of particuler letter in string

'''
To count how words are present in string equal to given letter(value). 
'''

myString="How many 'a' words in this string"

print(myString.count("o"))  #2 is answer
print(myString.count("w"))  #2 is answer
print(myString.count("i"))  #3  is answer
#you can count full world also

#to Capital first letter of string you can use Capitalize function

myCapital="varinder" # name will convert into capital letter by capital() function

print(myCapital.capitalize())

'''
To Find word is present in string equal to given letter(value). 
'''

myword="How many 'a' words in this string"

print(myword.find("many")) #it will tell us index number where word in present.
#like "many" is on index number 4.
print(myword.find("How"))
#like "How" is on index number 0.

'''
To Replace word is present in string equal to given letter(value). 
'''

myword="How many 'a' words in this string"

print(myword.replace("many","too many")) #it will tell us index number where word in present.
#like "many" is now  "too many".
print(myword.replace("How","Here"))
#like "How" is now "Here".

# to make change is big string
courseDetails='''
 <|NAME|> join <|COURSE|> course on <|DATE|>
 We hope <|COURSE|> is very easy for <|NAME|>  to learn .
 '''
name=input("Enter Name")
course=input("Enter Course")
date=input("Enter Date")
courseDetails=courseDetails.replace("<|NAME|>",name)
courseDetails=courseDetails.replace("<|COURSE|>",course)
courseDetails=courseDetails.replace("<|DATE|>",date)
print(courseDetails)