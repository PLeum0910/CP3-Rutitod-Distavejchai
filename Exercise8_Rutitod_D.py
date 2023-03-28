usernameinput = input("Username : ")
passwordinput = input("Password : ")
if usernameinput == "a1" and passwordinput == "1":
    print("----Welcome----")
    appleprice = 10
    bananaprice = 8
    orangeprice = 15
    print("1.Apple",appleprice,"THB")
    print("2.Banana",bananaprice,"THB")
    userselect = int(input(">>"))
    if userselect == 1:
        print("How many?")
        amount1 = int(input(">>"))
        print("Another One? (Y/N)")
        choose = str(input(">>"))
        if choose == "Y":
            print("1.Apple", appleprice, "THB")
            print("2.Banana", bananaprice, "THB")
            userselect1 = int(input(">>"))
            if userselect1 == 2:
                print("How many?")
                amount2 = int(input(">>"))
                print("Total :",amount1*appleprice+amount2*bananaprice,"THB")
        elif choose == "N":
            print("Total :", amount1 * appleprice, "THB")
    elif userselect == 2:
        print("How many?")
        amount2 = int(input(">>"))
        print("Another One? (Y/N)")
        choose = str(input(">>"))
        if choose == "Y":
            print("1.Apple", appleprice, "THB")
            print("2.Banana", bananaprice, "THB")
            userselect2 = int(input(">>"))
            if userselect2 == 1:
                print("How many?")
                amount1 = int(input(">>"))
                print("Total :",amount1*appleprice+amount2*bananaprice,"THB")
        elif choose == "N":
            print("Total :", amount2 * bananaprice, "THB")
else:
    print("Error")




