# Recursion

#find factorial of "n" number
#n=1*2*3*4*5=120 is factorial of 5

fact=5
factorial=1
for i in range(fact):
    factorial=factorial*(i+1)
print(factorial) #120 you will get in temrminal

#Now understand with function:
n=int(input('Enter number \n'))
def Factorial(n):
    start=1
    for i in range(n):
        start=start*(i+1)
    return start
print(f"Factorial of {n} in {Factorial(n)}  ")         
print(Factorial(n))

# Here write Recursive manner to do this with base condition:

def Recursive_Factorial(n):
    if n==1 or n==0:  #if n value is 1 or 0 then it will simple return 1 and stop working.
        return 1
    return n*Recursive_Factorial(n-1)     
print(f"Factorial of {n} in {Recursive_Factorial(n)}  ")         

#sum of natural numbers

def Recursive_Factorial(n):
    if n==1 or n==0:  #if n value is 1 or 0 then it will simple return 1 and stop working.
        return 1
    return n+Recursive_Factorial(n-1)     
print(f"sum of {n} in {Recursive_Factorial(n)}  ")  