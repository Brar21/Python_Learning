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