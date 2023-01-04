myDict={
    "name":"Varinder",
    "age":27,
    "work":"Content creater",
    "isStillworking":True,
    "Numbers":[1,23,4,56,7]
}
print(myDict) #print all elements of dictionary
print(myDict["age"])#print only age
print(myDict["work"])#print only work
print(myDict["isStillworking"])#print only working?
print(myDict["Numbers"])#print only numbers

 #name=key   #Varinder=value
#  *Data-Types you can put in Dictionary*
#  1. Interger("int")
#  2. Boolen ("bol")
#  3. String-Literal("str")
#  4. List("lst")
#  5. Dictionary("dic")  

#Dictionary in Dictionary Example:

myData={
    "name":"Varinder",
    "age":27,
    "Subjects":{"name":"Hindi","marks":75,"ispass":True}
}

print(myData["Subjects"]["name"])#to inside list you have write print like this


myData["Subjects"]["marks"]=100; #you can value very simple manner
print(myData["Subjects"]["marks"])


#what if key value pairs is not present in dictionary
myData["GoodInStudy"]=True #write key-value pair if that is not ther than it will automatically added
print(myData["GoodInStudy"])




print(myData.keys()) #now with this all keys will print

#to check type on keys
print(type(myData.keys()))


#to convert keys in list
print(list(myData.keys())) #insted "keys" write "list" than you get keys as list



#Print all value of Dictionary

print(myData.values()) #now with this all values will print

#to check type on keys
print(type(myData.values()))



#to convert values in list
print(list(myData.values())) #insted "values" write "list" than you get values as list


print(myData.items())#you get all items in form of tuple


#update key-value pair with new entery
newItem={
        "Mac-Book":"New_wish"
    } # you can add key-value pairs as much you want
myData.update(newItem)   #update new key-value in dictionary
print(myData) #now you can see new entry will be there

#print(myData.get("name"))
#print(myData.get("names")) # you got None

# .get() give value when you write key-name to get value but in case "Key-name" is not present then it show "None"

#print(myData["name"])
#print(myData["names"]) #you got error

# print(myData) in this case if "Key" is not present it will show error



# If user provide input then he get value of input example:

print(myData.keys())
UserEntery=input("Enter to search \n")
#print("Your results",myData[UserEntery])
# But if userEntery word is not in our Distionary then it will throug error but you have to tackle with error how?
# Use ".get()" rather than "[]" syntax
print(myData.get(UserEntery))