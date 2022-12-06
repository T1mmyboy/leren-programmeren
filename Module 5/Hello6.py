from ast import While
from distutils.command.build_scripts import first_line_re
import math
from re import A
def addition(eerste,tweede):
    resultaat = eerste+tweede
    print("",eerste,"+",tweede,"=",resultaat)
    return resultaat
def subtraction(eerste,tweede):
    resultaat = eerste-tweede
    print("",eerste,"-",tweede,"=",resultaat)
    return(resultaat)
def multiplication(eerste,tweede):
    resultaat = eerste * tweede
    print("",eerste,"x",tweede,"=",resultaat)
    return resultaat
def division(eerste,tweede):
    resultaat = eerste / tweede
    print("",eerste,":",tweede,"=",resultaat)
    return resultaat
firstround = True
berekeningen = True
teller = 0
antwoorden = ["a", "b", "c", "d", "e", "f","g","h","i"]
alles = True
opdracht = True
while opdracht == True:
    while firstround == True:
        choice = input("wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren? : ").lower()
        if choice not in antwoorden:
            print("Dat is geen optie!")
            continue
        while berekeningen == True:
            try:
                if teller <= 1:
                    getal = float(input("Welk getal? : "))
            except:
                print("U moet een getal invoeren!")
                continue
            if choice == "d" and getal == 0.0:
                print("Sneaky bastard")
                continue
            if choice == "a":
                if teller <=1:
                    if teller <1:
                        eerste = getal
                    teller = teller+1
                    continue
                resultaat = addition(eerste,getal)
                berekeningen = False
                firstround = False
            elif choice == "b":
                if teller <=1:
                    if teller <1:
                        eerste = getal
                    teller = teller+1
                    continue
                resultaat = subtraction(eerste,getal)
                berekeningen = False
                firstround = False
            elif choice == "c":
                if teller <=1:
                    if teller <1:
                        eerste = getal
                    teller = teller+1
                    continue
                resultaat = multiplication(eerste,getal)
                berekeningen = False
                firstround = False
            elif choice == "d":        
                if teller <=1:
                    if teller <1:
                        eerste = getal
                    teller = teller+1
                    continue
                resultaat = division(eerste,getal)
                berekeningen = False
                firstround = False
            elif choice == "e":
                tweede = 1.0
                resultaat = addition(getal,tweede)
                berekeningen = False
                firstround = False
            elif choice == "f":
                tweede = 1.0
                resultaat = subtraction(getal,tweede)
                berekeningen = False
                firstround = False
            elif choice == "g":
                tweede = 2.0
                resultaat = multiplication(getal,tweede)
                berekeningen = False
                firstround = False
            elif choice == "h":
                tweede = 2.0
                resultaat = division(getal,tweede)
                berekeningen = False
                firstround = False
            else:
                print("Dat is geen optie!")
                continue
    berekeningen = True
    while firstround == False:
        choice = input("wat wilt u doen met "+str(resultaat)+"? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren of I) stoppen? : ").lower()
        if choice not in antwoorden:
            print("Dat is geen optie!")
            continue
        if choice == "e":
            tweede = 1.0
            resultaat = addition(resultaat,tweede)
            continue
        elif choice == "f":
            tweede = 1.0
            resultaat = subtraction(resultaat,tweede)
            continue
        elif choice == "g":
            tweede = 2.0
            resultaat = multiplication(resultaat,tweede)
            continue
        elif choice == "h":
            tweede = 2.0
            resultaat = division(resultaat,tweede)
            continue
        elif choice == "i":
            print("Uw laatste antwoord was",resultaat)
            firstround = True
            opdracht = False
            break
        
        while berekeningen == True:
            try:
                getal = float(input("Welke getal? : "))
            except:
                print("Het moet een geldig getal zijn!")
            if choice == "d" and getal == 0.0:
                print("U kan niet delen met 0!")
                continue
            if choice == "a":
                resultaat = addition(resultaat,getal)
                break
            elif choice == "b":
                resultaat = subtraction(resultaat,getal)
                break
            elif choice == "c":
                resultaat = multiplication(resultaat,getal)
                break
            elif choice == "d":
                eerste = getal
                resultaat = division(resultaat,getal)
                break
            
            

