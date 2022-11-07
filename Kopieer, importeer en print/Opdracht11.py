from ast import Return
from cgitb import reset
from fruitmand import fruitmand
opnieuw = True
kleuren = []
lijstkleuren = []
for x in range(len(fruitmand)):
    lijstkleuren.append(fruitmand[x]["color"])
while opnieuw == True:
    kleur = input("Kies een kleur uit de kleuren Yellow/Orange/Green/Red/Brown : ").lower()
    if kleur not in lijstkleuren:
        continue
     
            
    for x in range(len(fruitmand)):
        
        if fruitmand[x]["color"] == kleur:
            kleuren.append(fruitmand[x]["round"])
    rond = kleuren.count(True)
    nietrond= kleuren.count(False)
    som = (rond-nietrond)
    if som <0:
        som = abs(som)
        print("er is",som, "meer niet ronde dan ronde van de kleur",kleur)
        break
    elif som >0:
        print("er is",som, "meer ronde dan niet ronde")
        break
    elif som == 0:
        print("er zijn evenveel ronde als niet ronde")
        break