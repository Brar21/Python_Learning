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
print(p.company)#than it will take from parent or Base class because in programers class no company is there


#Single Inheritance example is Above this line

