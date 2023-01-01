'''
for get only one word from string you can use "index" and index=length-1.
example=> length=5 then you can give index only 4 and index is always start from zero in every coding language.
how you write index of word see following example:
'''

name="Varidner"

print(name[0]) #[ ] this use for write index number like "name[0]" will print "V" 
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7]) 
''' 7 is last index-number if you try to print "name[8]" you got an error 
because index = length -1 means 8-1=7 are total index numbers present in string'''
#print(name[8])  

'''
if you want to print half of string then you ratio in []=>[0:4]
0 is indicate starting index and it will go less then 4 (0<4)
means it will print till [3] index number
'''

print(name[0:4])

#Print last index of following example string:

string="print last index of this string"

print(string[-1]) #then -1 will automatically print last index "g"