from logging.config import dictConfig
dicti = {}
opnieuw = True
print("Zeg ""'Stop'"" als u wilt stoppen""")
getal = 0
while opnieuw == True:
    vraag = input("Wat wilt u toevoegen? : ").capitalize()
    if vraag == "Stop":
        break
    aantal = input("Hoeveel "+vraag+" Wilt u? : ")
    try:
        aantal = int(aantal)
    except:
        print("Dat is geen getal!")
        continue
    else:
        
        if vraag not in dicti:
            dicti[vraag] = aantal
        
        else:
            dicti[vraag] = dicti[vraag] + aantal
                    
        continue
print("-------(Boodschappen)--------")
keeropnieuw = dicti.__len__()
nul = 0
sleutel = 0
cijfer = 1
first_pair = list(dicti.items())[nul]
for x in range(keeropnieuw):
    uhh = list(dicti.items())[nul]
    nul = nul +1
    key = uhh[sleutel]
    getal = uhh[cijfer]
    print("",getal,"x ",key)
print("------------------------------")




        