
# @property_decorators help you to take function as varible
class Employee:
        Name="varinder"
        Middle="Singh"
        Last="Brar"
        @property
        def name(self):
           return self.Name+" "+self.Middle+" "+self.Last
data=Employee()
print(data.name)  #here you get value from function write function as proporty