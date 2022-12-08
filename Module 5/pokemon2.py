from cgi import test
from itertools import repeat
from random import choice, randint
from time import sleep
import math
import random
thunderbolt = int(90)
scratch = int(40)
tackle = int(40)
psychic= int(95)
bite = int(60)
points = 0
first_time = False
opniew = True
sableye_moves = ["Scratch", "Psychic", "Bite", "Tackle"]
def intro():
    Naam = input("What is your name? ")
    print("Welcome",Naam,"to the world of Pokémon!")
    sleep(3)
    print("Your Pokémon companion is called a Sableye.")
    sleep(3)
    print("Sableye is a ghost/dark type Pokémon.")
    sleep(3)
    print("So its only Weakness is fairy type attacks.")
    sleep(3)
    print("Oh no! It looks like a wild Pikachu broke in!")
    sleep(3)
    print("You should fight the Pikachu with your new Sableye!")
    sleep(3)
    print("You can always try to run away from a fight, but it won't always work!")
    sleep(3)
    print("Or you could try to catch it with a Pokéball, but u should weaken it first!")
    sleep(3)
    print("You can earn points by either capturing a Pokémon or defeating it.")
    sleep(3)
    print("Fleeing doesn't grant any points.")
    sleep(3)
def randomgetal():
    getal = randint(1,4)
    print(getal)
    return getal    
def opnieuwspelen():
    x = 1
    while x == 1:
        choice = input("Do u want to play again? : ")
        if "yes" in choice:
            opnieuw = True
            x = 2
            return opnieuw
        elif "no" in choice:
            opnieuw = False
            x = 2
            return opnieuw
        else:
            print("thats not an option!")
            continue
while opniew == True:
    sableye_Hp = int(120)
    pikachu_Hp = int(120)
    helft_hp = pikachu_Hp/2
    print(pikachu_Hp)
    if first_time == True:
        intro()
    while pikachu_Hp >0 or sableye_Hp >0:
        choice = input("What will you do? Fight, Run or try to Catch it? : ").lower()
        sleep(1)
        if "catch" in choice:
            print("you throw a Pokéball!")
            if pikachu_Hp > helft_hp:
                #Meer dan 50% hp
                if randomgetal() == 4:
                    for x in range(1,4):
                        print("Shake",x)
                        sleep(1)
                    print("U caught the wild pikachu!")
                    if opnieuwspelen() == True:
                        first_time = False
                        break
                    else: 
                        opniew = False
                        break
                else:
                    for x in range(1,3):
                        print("Shake",x)
                        sleep(1)
                    print("Oh no the wild Pikachu broke out")
            else:
                #Minder dan 50% hp
                if randomgetal() >1:
                    for x in range(1,4):
                        print("Shake",x)
                        sleep(1)
                    print("U caught the wild pikachu!")
                    print("You gained 1 point!")
                    points=+1
                    pikachu_Hp = 0
                    if opnieuwspelen() == True:
                        first_time = False
                        break
                    else: 
                        print("You had",points,"points!")
                        quit()
                else:
                    for x in range(1,3):
                        print("Shake",x)
                        sleep(1)
                    print("Oh no the wild Pikachu broke out")
        elif "run" in choice:
            if randomgetal() == 1:
                points =+1
                print("You ran away!")
                if opnieuwspelen() == True:
                        first_time = False
                        break
                else: 
                    opniew = False
                    break
            else:
                print("You failed to run away!")
        elif "fight" in choice:
            while opniew == True:
                print("Your Sableye knows Scratch, Tackle, Bite and Psychic")
                move = input("Which move will you use? : ").capitalize()
                if move not in sableye_moves:
                    continue
                else:
                    print("Sableye used",move+"!")
                    if move == "Scratch":
                        pikachu_Hp = pikachu_Hp-scratch
                    elif move == "Tackle":
                        pikachu_Hp=pikachu_Hp-tackle
                    elif move == "Bite":
                        pikachu_Hp=pikachu_Hp-bite
                    elif move == "Psychic":
                        pikachu_Hp=pikachu_Hp-psychic
                    if pikachu_Hp <0:
                        pikachu_Hp = 0
                    print("Pikachu now has",pikachu_Hp,"HP")
                    
                    if pikachu_Hp == 0:
                        print("You defeated Pikachu!")
                        points =+1
                        print("You gained 1 point!")
                        if opnieuwspelen() == True:
                            first_time = False
                            break
                        else: 
                            print("You had",points,"points!")
                            quit()
                    break
        else:
            continue
        sleep(1)
        print("It is now the opponents turn!")
        sleep(1)
        randomcijfer = randomgetal()

        if randomcijfer == 4:
            if randomgetal() == 4:
                print("Pikachu ran away!")
                if opnieuwspelen() == True:
                    first_time = False
                    break
                else: 
                    print("You had",points,"points!")
                    quit()
                    
            else:
                print("Pikachu tried to run away!")
        elif randomcijfer == 1:
            print("Pikachu used Thunderbolt!")
            sableye_Hp = sableye_Hp-thunderbolt
        elif randomcijfer == 2:
            print("Pikachu used Bite!")
            sableye_Hp = sableye_Hp-bite
        elif randomcijfer == 3:
            print("Pikachu used Tackle!")
            sableye_Hp = sableye_Hp-tackle
        if sableye_Hp <0:
            sableye_Hp = 0
        sleep(1)
        print("Sableye now has",sableye_Hp,"HP")
        if sableye_Hp == 0:
            print("You were defeated by Pikachu!")
            if opnieuwspelen() == True:
                first_time = False
                break
            else: 
                print("You had",points,"points!")
                quit()
        

        






            

        
