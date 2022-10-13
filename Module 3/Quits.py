from webbrowser import get

opnieuw = True
teller = 0
while opnieuw == True:
    quits = input("?")
    teller = teller +1
    if quits == "quit" or quits == "quits":
        opnieuw = False
        print("",teller,"Keer tot Quits")
    else:
        opnieuw = True




