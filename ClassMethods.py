#class Methods

class IphonePrice:
    company="Apple"
    price=150
    location="Calefornia"

    def reducePrice(self,newprice):
        self.price = newprice

main=IphonePrice()
print(main.price)        #actual price will print
main.reducePrice(90)
print(main.price)    #it will print only function value only but not change actual value.
print(IphonePrice.price)