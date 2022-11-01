from __future__ import print_function
from faulthandler import dump_traceback
from random import randint, shuffle
import random


kaartkleur = ["Harten", "Klaveren", "Schoppen", "Ruiten"]
kaartsoort = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Boer", "Vrouw", "Heer", "Aas"]
deck = ["Joker","Joker",]
nummer = 1
for i in range(len(kaartkleur)):
    for j in range(len(kaartsoort)):
        deck.append(kaartkleur[i]+ " "+ kaartsoort[j])
shuffle(deck)
for x in range(7):
    print("Kaart",nummer, ":",deck[x])
    nummer = nummer +1
    deck.pop(x)
print("Deck van",len(deck), "kaarten: ",deck)



