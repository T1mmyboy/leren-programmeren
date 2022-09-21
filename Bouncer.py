from time import sleep

Leeftijd = input("Wat is uw leeftijd? ")
sleep(1)
Leeftijd = int(Leeftijd)
if Leeftijd >= 18:
    print("U mag naar binnen.")
    sleep(1)
    naam = input("Wat is uw naam? ")
    sleep(1)
    if Leeftijd <21:            
            if naam == "Rudi":
                print("Sticker")
                drinken = input("Wat wilt u drinken? A)Bier of B)Cola?")
                if drinken == "A":
                    print("U bent te jong voor dat!")
                elif drinken == "B":
                    print("Dat is dan gratis!")
            elif naam == "Arnold":
                print("Sticker")
                drinken = input("Wat wilt u drinken? A)Bier of B)Cola?")
                if drinken == "A":
                    print("U bent te jong voor dat!")
                elif drinken == "B":
                    print("Dat is dan gratis!")
            
            elif naam == "Jeroen":
                print("Sticker")
                drinken = input("Wat wilt u drinken? A)Bier of B)Cola?")
                if drinken == "A":
                    print("U bent te jong voor dat!")
                elif drinken == "B":
                    print("Dat is dan gratis!")
            
            elif naam == "Kjeld":
                print("Sticker")
                drinken = input("Wat wilt u drinken? A)Bier of B)Cola?")
                if drinken == "A":
                    print("U bent te jong voor dat!")
                elif drinken == "B":
                    print("Dat is dan gratis!")
            else :
                print("U mag naar binnen maar u krijgt geen bandje om alcohol te halen.")
                drinken = input("Wat wilt u drinken? A)Bier of B)Cola?")
                if drinken == "A":
                    print("U bent te jong voor dat!")
                elif drinken == "B":
                    print("Dat wordt dan $1,00")
    
    
    elif Leeftijd >= 21:
        print("U mag naar binnen met een armbandje.")   
        drinken = input("Wat wilt u drinken? A)Bier of B)Cola?")
else: 
    print("U bent te jong, u mag niet naar binnen.")
    drinken = input("Wat wilt u drinken? A)Bier of B)Cola?")
    if drinken == "A":
        print("Dat wordt dan $1,50")
    elif drinken == "B":
        print("Dat wordt dan $1,00")