menulist = []

def Showbill():
    print("--- My Food ---")
    for number in range(len(menulist)):
        print(menulist[number][0],menulist[number][1])

while True:
    menuname = input("Please Enter Menu : ")
    if(menuname.lower() == "exit"):
        break
    else:
        menuprice = input("Price : ")
        menulist.append([menuname,menuprice])
Showbill()