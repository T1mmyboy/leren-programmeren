from typing import Counter


List = []
Dicti = {}
opnieuw = True
while opnieuw == True:
    vraag = input("Wilt u iets toevoegen? ja/nee : ").capitalize()
    if vraag == "Ja":
        item = input("Wat wilt u toevoegen : ").capitalize()
        
        aantal = input("Hoeveel "+item+" Wilt u? : ")
        combo =(aantal+"x "+item)
        List.append(combo) 
    else:
        print("-(BOODSCHAPPENLIJST)-")
        for x in List:
            print(x)
            opnieuw = False
        print("---------------------")