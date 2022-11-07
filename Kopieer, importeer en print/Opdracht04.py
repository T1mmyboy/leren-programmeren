from fruitmand import fruitmand
import random
fruitnaam = []
mand = []
aantal = int(input("Hoeveel fruit wilt u in uw fruitmand? : "))
for x in range(len(fruitmand)):
    fruitnaam.append(fruitmand[x]["name"])


for x in range(aantal):
    fruiten = random.choice(fruitnaam)
    mand.append(fruiten)
print("In uw mand zit: ",mand)

