# for sort list in correct manner
a=[1,8,5,9,7,3,6,4,2] 
'''
for make it in right order.
like 1,2,3...9
you can use .sort() method
'''
#print(a.sort()) 
#you will get "NONE" you know reason behind this
#because this is wrong way to write code for sorting
#you have to write like this:

a.sort() #now list will be sorted.you can print it.
print(a) #list in Assending order

#Print list reverse or Dessending order

a.reverse() #list start arrange from last to first
print(a) #now List in dessending order