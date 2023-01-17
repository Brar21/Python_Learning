#operator_overloading using dunder methods

class Number:
    def __init__(self,num):
        self.num= num
    
    def __add__(self,num2):#this is example of dunder methods
        print("Let add")
        return self.num+num2.num
    
    def __add__(self,num2):#this is example of dunder methods
        print("Let minus")
        return self.num-num2.num
    
    def __add__(self,num2):#this is example of dunder methods
        print("Let Multiply")
        return self.num*num2.num
    
    def __add__(self,num2):#this is example of dunder methods
        print("Let divide")
        return self.num/num2.num
n1=Number(4)
n2=Number(6)
sum=n1+n2
print(sum)
    
        