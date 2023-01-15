#class Methods

class IphonePrice:
    company="Apple"
    price="150k"
    location="Calefornia"

    #def reducePrice(self,newprice):
    #    #self.price = newprice #first method to change class price
    #    self.__class__.price=newprice #now class price also change with newprice
 #another way to do this
 # "@classmethod"
    @classmethod
    def reducePrice(self,newprice):
        self.price=newprice #price will change same as we d with above way I showed you
main=IphonePrice()
print(main.price)        #actual price will print
main.reducePrice("80k")
print(main.price)    #it will print only function value only but not change actual value.
print(IphonePrice.price) #but question is how to change class attribute price?