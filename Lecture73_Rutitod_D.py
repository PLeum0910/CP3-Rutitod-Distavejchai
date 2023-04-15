systemmenu = {"ข้าวหมกไก่":45,"ข้าวมันไก่":40,"ข้าวมันไก่ผสม":50,"ข้าวมันไก่พิเศษ":45}
menulist =[]
def Showbill():
    totalprice = 0
    print("--- My Food ---")
    for number in range(len(menulist)):
        print(menulist[number][0],menulist[number][1])
        totalprice += int(menulist[number][1])
    print("Total :", totalprice)

while True:
    menuname = input("Please Enter Menu : ")
    if(menuname.lower() == "exit"):
        break
    else:
        menulist.append([menuname,systemmenu[menuname]])
print(menulist)
Showbill()