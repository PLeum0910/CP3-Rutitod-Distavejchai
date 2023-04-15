menulist = []
pricelist = []

def Showbill():
    totalprice = 0
    print("--- My Food ---")
    for number in range(len(menulist)):
        print(menulist[number],pricelist[number])
        totalprice += int(pricelist[number])
    print("Total :",totalprice)

while True:
    menuname = input("Please Enter Menu : ")
    if(menuname.lower() == "exit"):
        break
    else:
        menuprice = input("Price : ")
        menulist.append(menuname)
        pricelist.append(menuprice)
Showbill()