from __future__ import print_function
from faulthandler import dump_traceback
from random import randint
import random


kaartkleur = ["Harten", "Klaveren", "Schoppen", "Ruiten"]
kaartsoort = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Boer", "Vrouw", "Heer", "Aas"]

deck = ["joker", "Joker",]
nummer = 1
for x in range(47):
    kaart = random.choice(kaartkleur)
    soort = random.choice(kaartsoort)
    eenkaart = (kaart,soort)
    deck.append(eenkaart)
random.shuffle(deck)
for x in range(7):
    print("Kaart", nummer, ":",deck[nummer])
    nummer = nummer +1
print("Deck van 47 Kaarten:", deck)
    




