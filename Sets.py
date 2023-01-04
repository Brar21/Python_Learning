a={1,2,3,4,5,6,6}
print(a)
'''as i mention in note set i collection of non-repititive elements when you print this you can see
only one  6 is printed second is ignore by default
'''

#for Print type when print(type(a)) you get "set"
print(type(a))



#Importent for create empty set
'''a={} this will make empty Dictionary
print(type(a)) then you get class ="dict"
so,this i wrong way
'''

# An empty set can be created like this below syntax:

Empty_set=set() #set is created you can check type of this 
print(type(Empty_set)) #you can se type is class="set"


#METHODS of Sets:

#Now you can add element as below shown but can't add duplicate element rember that
# ".add()" will help us to add value or element
Empty_set.add(1)
Empty_set.add(1)# i did this just for showing you that you can't add duplicate
Empty_set.add(2)
Empty_set.add(3)
Empty_set.add(4)

print(Empty_set)# all elements are add and "1" come only one time you see

# to print length of "Set" use "len" method as shown below:

print(len(Empty_set)) #you get length "4" of this set


# for "Remove" element from set use ".remove()" check below example:

Empty_set.remove(3) # we remove "3" from set
print(Empty_set) # "3" is removed from Set.

# if Value or Element is npot presnt in set and you try to remove than it will through an error that element keyerror:(value)

#Empty_set.remove(6) #error= keyerror:6 becasue 6 is not in my set
#print(Empty_set)

# ".pop()" to remove first element from set
print(Empty_set.pop())# "1" is removed from starting of set
print(Empty_set)# left element are print