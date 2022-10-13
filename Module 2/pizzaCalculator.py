from ast import If
from logging.handlers import TimedRotatingFileHandler
import math
from tracemalloc import stop

#Tim van der wulp
#99074833
#opdracht Pizzacalculator
small=6.99
medium=9.99
large=12.99

keuze = input("Wilt u een small of medium of large pizza :")
aantal = input("hoeveel pizza's wilt u :")

if keuze == "small":
    try:
        prijs = int (aantal)*6.99
    except:
        print("Dat is geen cijfer!")
        stop
if keuze == "medium":
    try:
        prijs = int (aantal)*9.99
    except:
        print("Dat is geen cijfer!")
        stop
if keuze =="large":
    try:
        prijs= int (aantal)*12.99
    except:
        print("Dat is geen cijfer!") 

print("""|uw totale bedrag is""",prijs,""" van""" ,aantal,keuze,"""pizza's" |""")

