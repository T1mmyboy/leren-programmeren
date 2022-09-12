from importlib import import_module
import math 
ppl = input("Met hoeveel mensen gaat u: ")
toegangsticket = int (ppl) *7.45
a = 5
tijd_in_vr = input ("Hoelang wilt u VR: ")
prijs = int (tijd_in_vr) / int (a)
Vrbril = int (0.37*prijs)
totaal = (int (Vrbril)+ int (toegangsticket) * int (ppl))
print("Dit geweldige dagje-uit met" ,ppl,"mensen in de Speelhal met" ,tijd_in_vr, "minuten VR kost je maar" ,totaal, "euro!")


