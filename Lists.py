a=[1,2,5,1,546] #lists are same as arrays in javascript
print(a) #a is "int" list (integers).
print(a[4]) #for print particuler one index
# we change the value of particuler position
a[2]=3
a[3]=4
a[4]=5
#now list will look like: [1,2,3,4,5]
print(a)
b=[True,False,True,True] #list of booleans "bol"
print(b)
print(b[1])#for print particuler one index
# same as "int" list you can value or boolean "bol" list
#example change index[1] "false" to "true"
b[1]=True
print(b) #now all list of "bol" is "true" value
print(len(b)) #Length can also check by len(). function

#slicing in list 
print(b[0:3])
#print(b[0:3:2])