usernameinput = input("Username : ")
passwordinput = input("Password : ")
if usernameinput == "a1" and passwordinput == "1":
    print("----Welcome----")
    appleprice = 10
    bananaprice = 8
    orangeprice = 15
    print("1.Apple",appleprice,"THB")
    print("2.Banana",bananaprice,"THB")
    print("What do you want?")
    userselect = int(input(">>"))
    if userselect == 1:
        print("How many?")
        amountapple = int(input(">>"))
        print("Another One? (Y/N)")
        choose = str(input(">>"))
        if choose == "Y":
            print("1.Apple", appleprice, "THB")
            print("2.Banana", bananaprice, "THB")
            userselect1 = int(input(">>"))
            if userselect1 == 2:
                print("How many?")
                amountbanana = int(input(">>"))
                print("Total :",amountapple*appleprice+amountbanana*bananaprice,"THB")
                print("Thanks for Shopping")
        elif choose == "N":
            print("Total :", amountapple * appleprice, "THB")
            print("Thanks for Shopping")
    elif userselect == 2:
        print("How many?")
        amountbanana = int(input(">>"))
        print("Another One? (Y/N)")
        choose = str(input(">>"))
        if choose == "Y":
            print("1.Apple", appleprice, "THB")
            print("2.Banana", bananaprice, "THB")
            userselect2 = int(input(">>"))
            if userselect2 == 1:
                print("How many?")
                amountapple = int(input(">>"))
                print("Total :",amountapple*appleprice+amountbanana*bananaprice,"THB")
                print("Thanks for Shopping")
        elif choose == "N":
            print("Total :", amountbanana * bananaprice, "THB")
            print("Thanks for Shopping")
else:
    print("Error")