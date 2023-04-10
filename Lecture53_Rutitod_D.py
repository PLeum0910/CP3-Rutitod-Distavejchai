def vatcal(totalprice = int(input("Enter price : "))):
    result = totalprice+(totalprice*7/100)
    return result
print(vatcal())
