##n = int(input().strip())

###if (n==0 or n==1):
###    print("Weird")
##if (n%2)==0 and n>=2 and n<5:
##        print("Not Weird")    

##if (n%2)==0 and n>=6 and n<=20:
##     print("Weird")        
  
##if (n%2)==0 and n>20:
##    print("Not Weird") 
##if (n%2)==1:
##    print("Weird")    

##a=3
##b=5
###if(a<b):
###    print(a+b)
###if(b>a):
###    print(a-b)
###if(b>=a):
###    print(a*b)        

##print(a//b)
##print(a/b)
##n=int(input())
###print(n[0]*n[0])
###print(n[1]*n[1])
###print(n[2]*n[2])
###for print sequare of list number in next new line
##for i in range(0, 100):
##    if i<n:
##     print(i*i)

#def is_leap(year):
##if year%4==0:
##  leap=True
##elif year%100== 0:
##    leap=False 
##elif year%400==0:
##    leap=True
#    leap = False 
#    leap = year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 ==0
#    if leap:
#        return leap
#    else:
#        return leap    
#year = int(input())
#print(is_leap(year))

#HackerRank Set .discard(), .remove() & .pop() in python problem solution

#n = int(input())
#s = set(map(int, input().split()))

#length = int(input())

#for i in range(0, length):
#    kwargs = input().strip().split(" ")
#    if kwargs[0] == "pop":
#        s.pop()
#    elif kwargs[0] == "remove":
#        s.remove(int(kwargs[1]))
#    elif kwargs[0] == "discard":
#        s.discard(int(kwargs[1]))
        
#Hello good night        
   
#print (sum(s))

#to count union, intersection, diffrence,symmetric_diffrence in hanker rank question

#n,a = int(input()),set(int(i) for i in input().split())
#m,b = int(input()),set(int(i) for i in input().split())
#print(len(a.union(b)))