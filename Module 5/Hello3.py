nummer = int(input("Van welk getal wilt u de tafel zien? : "))
def tafel():
    for x in range(1,11):
        resultaat = nummer * x
        print(x,"x", nummer, "=",resultaat)
tafel()