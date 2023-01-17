#operator_overloading using dunder methods

class Number:
    def __init__(self,num):
        self.num= num
    
    def __add__(self,num2):#this is example of dunder methods for add overload load
        print("Let add")
        return self.num+num2.num
    
    def __sub__(self,num2):#this is example of dunder methods for minus overload
        print("Let minus")
        return self.num-num2.num
    
    def __mul__(self,num2):#this is example of dunder methods for multiply overload
        print("Let Multiply")
        return self.num*num2.num
    
    def __truediv__(self,num2):#this is example of dunder methods for divide overload
        print("Let divide")
        return self.num/num2.num 
    
n1=Number(12)
n2=Number(6)
sum=n1+n2
multi=n1*n2
minus=n1-n2
divide=n1/n2
print(sum)
print(minus)
print(multi)
print(divide)

    
        