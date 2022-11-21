from random import randint
import random
kleuren = ["Oranje", "Blauw", "Groen", "Blauw"]
aantal = int(input("Hoeveel M&Ms wilt u? "))
zak = []
for x in range(aantal):
    kleurenzak = random.choice(kleuren[0:3])
    zak.append(kleurenzak)
print("U heeft een zak met",zak,"M&Ms")

    


