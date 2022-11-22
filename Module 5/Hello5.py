
def deRest(aantal):
    nummers = []
    nieuwgetal = 1
    oudgetal = 1
    nummers.append(0)
    nummers.append(nieuwgetal)
    nummers.append(oudgetal)
    for x in range(aantal):
        resultaat = nummers[-2]+nummers[-1]
        nummers.append(resultaat)
    print(nummers)
deRest(5)
