from random import shuffle
teller = 0
namen = []
opnieuw = True
while opnieuw == True:
    naam = input("Hoe heet de deelnemer? : ").capitalize()
    if naam not in namen:
        namen.append(naam)
        while opnieuw == True:
            keuze = input("Wilt u nog een deelnemer toevoegen? : ").lower()
            if keuze == "nee":
                if len(namen) >=3:
                    shuffle(namen)
                    for x in range(len(namen)-1):
                        print(namen[teller],"Heeft",namen[teller+1])
                        teller = teller +1
                    print(namen[teller],"Heeft",namen[0])
                    quit()
                else: 
                    print("U heeft minimaal 3 personen nodig!")
                    break
            elif keuze == "ja":
                break
            else:
                print("U moet Ja of Nee zeggen!")
                continue
    else:
        print("Die persoon zit er al in! ")