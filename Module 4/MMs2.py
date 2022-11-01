from fnmatch import translate
from random import randint
import random
kleuren = ["Rode M&Ms", "Blauwe M&Ms", "Groene M&Ms", "Gele M&Ms", "Bruine M&Ms"]
try:
    aantal = input("Hoeveel M&Ms wilt u? ")
    aantal = int(aantal)
except:
    print("Dat is geen getal!")
    quit()
zakMM = {
    "Rode M&Ms" : 0,
    "Blauwe M&Ms" : 0,
    "Groene M&Ms" : 0,
    "Gele M&Ms" : 0,
    "Bruine M&Ms" : 0
}
for y in range(aantal):
    kleurenzak = random.choice(kleuren)
    zakMM[kleurenzak] = zakMM[kleurenzak]+1
print(zakMM) 
        