#operator_overloading using dunder methods

class Number:
    def __init__(self,num):
        self.num= num
    
    def __add__(self,num2):#this is example of dunder methods
        print("Let add")
        return self.num+num2.num
    
    def __sub__(self,num2):#this is example of dunder methods
        print("Let minus")
        return self.num-num2.num
    
    def __mul__(self,num2):#this is example of dunder methods
        print("Let Multiply")
        return self.num*num2.num
    
    #def __div__(self,num2):#this is example of dunder methods
    #    print("Let divide")
    #    return self.num+num2.num / 2
    
n1=Number(12)
n2=Number(6)
sum=n1+n2
multi=n1*n2
minus=n1-n2
#divide=n1+n2/Number(2)
print(sum)
print(minus)
print(multi)
#print(divide)

    
        