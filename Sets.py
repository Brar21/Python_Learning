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

#Now you can add element as below shown but can't add duplicate element rember that
# ".add()" will help us to add value or element
Empty_set.add(1)
Empty_set.add(1)# i did this just for showing you that you can't add duplicate
Empty_set.add(2)
Empty_set.add(3)
Empty_set.add(4)

print(Empty_set)# all elements are add and "1" come only one time you see
