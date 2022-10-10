from random import randint
from time import sleep
#de computers getal
ronde = 1
ronde = int(ronde)
poging = 0
poging = int(poging)
print("er zijn 20 rondes.")
sleep(1)
print("in iedere ronde heb je 10 kansen.")
while ronde <20:
    random_getal = randint(1,100)
    while poging < 10:
        print(random_getal)
        try:
            jou_keuze = (int(input("Welk getal denkt u dat het is? ")))
        except:
            quit()
        som = abs(jou_keuze - random_getal)
        if som <=50 and som >30:
            print("Je bent koud")
        elif som <=30 and som >20:
            print("je bent warm")
        elif som <=20 and som >10:
            print("Je bent warmer")
        elif som <=10 and som >5:
            print("Je bent MEGA warm")
        elif som  <=5 and som >0:
            print("Je bent ON FIREEE") 
        elif som == 0: 
            print("U heeft het goed geraden!")
            print("u heeft het in",poging,"keer gegokt")
            break
        else:
            print("raad nog maar een keer")
        poging = poging +1
        print("poging ",poging,"")
    print("Het getal was",random_getal,)
    ronde = ronde +1
    print("u bent bij ronde",ronde,"")
    poging = 0





