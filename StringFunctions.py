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
