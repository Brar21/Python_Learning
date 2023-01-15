#inheritance

class Emplyoee:
    company="JavascriptFolks"

    def showDetails(self):
        print("Emplyoee Data")

class Programers(Emplyoee):
      language="Python"
      def getlanguage(self):
        print(f"this language is {self.language}")
e=Emplyoee()
e.showDetails()
p=Programers()
p.showDetails()     #it will print smae details of Emplyoee class
#because Programers claa has now details so it will take from Parent or Base class value   
#if you print language of Programers class
p.getlanguage()#you get "python" because language is present there
#print(p.company)#than it will take from parent or Base class because in programers class no company is there


#Single Inheritance example is Above this line

#Multiple Inheritnace

class EmployeeData:
    company="JavascriptFolksstartup"
    def NamesofEmployees(self):
        print(f"Employee name is{self.name}")

class Joblevel:
    SED_level="level 1"

class IndvidualData(EmployeeData,Joblevel):
    name="Varinder Brar"

p=EmployeeData()
p=IndvidualData()
print(p.name)
print(p.company)


#Multi-level Inheritance
 
class FamilyTree:#parent class
    surname="Brar"
    def Headname(self):
        print(f"Head of {self.name}")

class TreeBranch(FamilyTree):#child class of Familytree and parent of Newfamilyhead
    mainBranch="Parmjite kaur Brar"
    number=5
    def Children(self):
        print(f"Childs in Family {self.number}")

class NewFamilyHead(TreeBranch):#chlid class of Treerbanch clas
    Headname="Gurinder Brar"

    def NewFamilymembers(self):
        print(f'{self.number-1} Family members')

h=FamilyTree()
Sh=TreeBranch()
#Sh.number=5
n=NewFamilyHead()
print(n.surname)
print(n.mainBranch)
Sh.Children()
n.NewFamilymembers()