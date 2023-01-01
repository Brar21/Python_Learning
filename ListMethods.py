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

#a.reverse() #list start arrange from last to first
#print(a) #now List in dessending order


#Append to add something in the end of list
a.append(10) #to add 10 at the end of list
print(a) #10 added in the end of list you can see

a.insert(9,0) #to add 0 at 9th index number you use insert
print(a) #0 added at 9th index and 10 move to 10th index

a.pop()#it will delete last item of index
print(a)#10 id deleted from last

a.pop(2)#if you provide index number to delete item then item on that indexnumber willbe deleted
print(a)#like on index 2 item number-3 is deleted

a.remove(0) #here you provide value=0 to remove from list
print(a)#zero is removed from list

#person name list
#simple way to make list with input() function

p1=input("Enter Person Name \n")
p2=input("Enter Person Name \n")
p3=input("Enter Person Name \n")
p4=input("Enter Person Name \n")

personList=[p1,p2,p3,p4]
print(personList)
 
 #student marks store and print in assending order

student1=int(input("Enter Marks \n"))
student2=int(input("Enter Marks \n"))
student3=int(input("Enter Marks \n"))
student4=int(input("Enter Marks \n"))
marksList=[student1,student2,student3,student4] #first store by use input function
marksList.sort()#sort in assending order by sort() function
print(marksList)#print it
