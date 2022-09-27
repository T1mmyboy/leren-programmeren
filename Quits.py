from webbrowser import get


getal = input("Hoeveel keer is quits? ")
getal = int(getal)
gelijk = False
punt = 0
punt = int(punt)
while gelijk == False:
    if punt < getal:
        print("?")
        punt = punt +1
        gelijk = False
    else:
        print("dat waren",punt,"vraagtekens")
        gelijk = True


