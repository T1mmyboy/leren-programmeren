from ast import If
from logging.handlers import TimedRotatingFileHandler
import math

#Tim van der wulp
#99074833
#opdracht Pizzacalculator
small=6.99
medium=9.99
large=12.99

keuze = input("Wilt u een small of medium of large pizza :")
aantal = input("hoeveel pizza's wilt u :")

if keuze == "small":
    prijs = int (aantal)*6.99

if keuze == "medium":
    prijs = int (aantal)*9.99
    
if keuze =="large":
    prijs= int (aantal)*12.99

print(" ----------------------------")   
print("""|uw totale bedrag is""",prijs,""" van""" ,aantal,keuze,"""pizza's" |""")
print(" ----------------------------") 
