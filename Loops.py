#Loops is very importent role in coding

inital =0
#while inital>10 :
    #print("yes")  #nothing will happen because "0 can never bigger than 10"
    #but if we reverse the condition "initial<10" than infinity loop will start which never stop
    # to stop that loop on somewhere you have to provide  some case or condition to it
    #like
while inital<10 :
    print("yes" + str(inital))  #now "yes" print 5 time than loop stop becasue after that initial become bigger than 10

    inital=inital+2

#More exmples
#print counting unitl 50
i=1
while i<=50:
    print(i)
    i=i+1

#print list with while loop

l1=["Raju","Sonu","Deepti","Sonia","Kunal"]
i=0
while i<len(l1):
    print(l1[i])
    i=i+1  # is question comes in your mind why we wrote every time "i=i+1". "Nahi!" toh lao thodi "ruchi" lao isme...
    # if you not give the increment in value than how you will come out from loop. because if value is true than it never will stop
    # fir ant-man ki traha quantum face mein attk jaoge.
    # to come out from loop hume value ko badna hai ta jo hmari conditon false ho or hmari jann chutte isse.


# For loop syntac with example:
# 
Table=[1,2,3,4,6,8]
for item in Table: #"item" help us to do work in one-shot
    print(item)    #mujhe pta hai khoge yeh bhbut asan tha yr "while" to kafi tedda hai


#try to print "li" list which is on line number 23.

for item in l1:
    print(item) #yeh kya sirf ek line k code me hogya or while mein teen line baap re! "Raju" dekh re baba kya zhol ho rha hai idder!