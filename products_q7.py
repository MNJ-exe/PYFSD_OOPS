class products:
    def __init__(self,name,price):
        self.name=name
        self.price=price
p1=products("laptop",100000)
p2=products("mouse",1000)
print(p1.name,"of price",p1.price)
print(p2.name,"of price",p2.price)



# class products:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def pr(self):
#         print(self.name,"of price",self.price)
# p1=products("laptop",100000)
# p2=products("mouse",1000)
# p1.pr()
# p2.pr()