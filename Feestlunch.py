from importlib import import_module
import math
Acroissant = input("Hoeveel Croissants: ")
Astok = input("Hoeveel Stokbroden: ")
Akorting = input("Hoeveel Kortingsbonnen heeft u: ")
Korting = int (Akorting)*0.50
stokbrood = int (Astok) *2.78
croissant = int (Acroissant) *0.39

Eind = (int (croissant) + int (stokbrood) - int (Korting))


print("De feestlunch kost je bij de bakker" ,Eind, "euro voor de" ,Acroissant, "croissantjes en de",Astok, "stokbroden als de",Akorting, "kortingsbonnen nog geldig zijn!")