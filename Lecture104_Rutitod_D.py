class Customer:
    name = ""
    lastname = ""
    age = 0

    def addcart(self):
        print("Added product to",self.name,self.lastname,"cart")

customer1 = Customer()
customer1.name = "Rutitod"
customer1.lastname = "Distavejchai"
customer1.addcart()

customer2 = Customer()
customer2.name = "Pitikorn"
customer2.lastname = "Moonchob"
customer2.addcart()

customer3 = Customer()
customer3.name = "Chinatip"
customer3.lastname = "Keawruk"
customer3.addcart()

customer4 = Customer()
customer4.name = "Krittin"
customer4.lastname = "Sinnoy"
customer4.addcart()