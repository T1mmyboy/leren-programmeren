from random import randint
#de computers getal
random_getal = randint(1,1000)
ronde = 1
ronde = int(ronde)

while ronde < 20:
    try:
        jou_keuze = (int(input("Welk getal denkt u dat het is? ")))
    except:
        print("Dat is geen optie!")
        continue
    som = abs(jou_keuze - random_getal)
    if som <=500 and som >300:
        print("Je bent koud")
    elif som <=300 and som >200:
        print("je bent warm")
    elif som <=200 and som >100:
        print("Je bent warmer")
    elif som <=100 and som >50:
        print("Je bent MEGA warm")
    elif som  <=50 and som >25:
        print("Je bent ON FIREEE") 
    elif som <=25 and som >0:
        print("ER IS VUUR")
    elif som == 0: 
        print("U heeft het goed geraden!")
        print("u heeft het in",ronde,"keer gegokt")
        quit()
    else:
        print("raad nog maar een keer")
    ronde = ronde +1
    print("ronde ",ronde,"")
    
print("Het getal was",random_getal,)



