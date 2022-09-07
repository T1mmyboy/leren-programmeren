from importlib import import_module
import math
Acroissant = 17
croissant = 0.39*Acroissant
Astok = 2
stokbrood = 2.78*Astok
Akorting = 3
Korting = 0.50*Akorting
Eind = croissant+stokbrood-Korting
print(croissant+stokbrood-Korting)
print("De feestlunch kost je bij de bakker" ,Eind, "euro voor de" ,Acroissant, "croissantjes en de",Astok, "stokbroden als de",Akorting, "kortingsbonnen nog geldig zijn!")