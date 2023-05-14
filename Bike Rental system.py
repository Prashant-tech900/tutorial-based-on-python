#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class bikeshop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("total Bikes",self.stock)
    def rentforBike(self,q):
        if q<=0:
            print("Enter the value gether than 0")
        elif q>self.stock:
            print("Enter the value less then stock")
        else:
            self.stock=self.stock-q
            print("total prices",q*100)
            print("total Bike",self.stock)
while True:
    obj=bikeshop(100)
    uc=int(input('''
    1. Display
    2. Rent a bike
    3. Exit
    '''))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter the quantity:- "))
        obj.rentforBike(n)
    else:
        break


# In[ ]:




