 
class FamilyTree:#parent class
    surname="Brar"
    Head="Ranbir Singh Brar"
    def __init__(self):
        print(f"Family Start from {self.Head} \n")

    def HeadName(self):
        print(f"Head of {self.Head}")

class TreeBranch(FamilyTree):#child class of Familytree and parent of Newfamilyhead
    mainBranch="Parmjite kaur Brar"
    number=5
    

    def Children(self):
        print(f"Childs in Family {self.number}")

class NewFamilyHead(TreeBranch):#chlid class of Treerbanch clas
    Headname="Gurinder Brar"
    def __init__(self):
      super().__init__()#with this we can use constructor of parent class
      print(f"Family Start from {self.Headname} \n")

    def NewFamilymembers(self):
        print(f'{self.number-1} Family members')

    def HeadName(self):
        super().HeadName()
        print(f"{self.Headname} is ne familyhead")        

#h=FamilyTree()
#Sh=TreeBranch()
#Sh.number=5
n=NewFamilyHead()
#print(n.surname)
#print(n.mainBranch)
#Sh.Children()
#n.NewFamilymembers()
#print(n.Headname)#this will print only child class headname
#n.HeadName()#this will print first main or parent class headname after its own headname
