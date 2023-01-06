#Range function in Python
#first example you see in  "Loops.py" file and why it start from zero you may learn there
# if you want to start from you choice number than can do like this:

for i in range(5,11):
        print(i)
# in this example number start printing from 5 and print till 10 means in between 5 to 11
#  5 is starting point and upto 11 meas "11" is edn point
# Now how you can skip numbers between than
# Note you can set after first print how many number you want to skip every time#
# Example is shown below
for i in range(1,10,2):
    print(i) # after print number two number you skipping in this example


# For loop with else condition 
# when if condition done his work it will print

for i in range(12):
    print(i)
else:
    print("after done for loop condtion do this "+str(i+1))         