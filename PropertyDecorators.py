
# @property_decorators help you to take function as varible
class Employee:
        Name="varinder"
        pocktmoney=5004
        saving=5000
        @property
        def totalmoney(self):
           return self.pocktmoney+self.saving

        @totalmoney.setter   
        def totalmoney(self,value):
            self.saving=value-self.pocktmoney
data=Employee()
print(data.totalmoney)  #here you get value from function write function as proporty
data.totalmoney=9999
print(data.saving)
print(data.totalmoney)
#if you want to set return value according to your need
 