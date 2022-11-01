from typing import Counter


List = []
Dicti = {}
opnieuw = True
while opnieuw == True:
    vraag = input("Wilt u iets toevoegen? ja/nee : ").capitalize()
    if vraag == "Ja":
        item = input("Wat wilt u toevoegen : ").capitalize()
        aantal = input("Hoeveel "+item+" Wilt u? : ")
        List.append(aantal, "x", item)
        
    else:
        Dicti = dict.fromkeys(List)
        print("-(BOODSCHAPPENLIJST)-")
        for x in Dicti:
            print(x)
            opnieuw = False
        print("---------------------")