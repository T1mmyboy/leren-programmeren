from itertools import repeat
from random import choice
from time import sleep
import math
import random


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

thunderbolt = 90
thunderbolt = int(thunderbolt)
sableye_Hp = 90
sableye_Hp = int(sableye_Hp)
Pikachu_Hp = 80
Pikachu_Hp = int(Pikachu_Hp)
scratch = 40
scratch = int(scratch)
tackle = 40 
tackle = int(tackle)
psychic= 95
psychic = int(psychic)
bite = 60 
bite = int(bite)
pikachu_dead = False
sableye_dead = False
while pikachu_dead == False or sableye_dead == False:
    
    if Pikachu_Hp <=0:
        pikachu_dead = True
        if pikachu_dead == True:
            print("You defeated Pikachu!")
            quit()
    fightorflight = input("What will you do? fight or run? ").lower()
    if fightorflight == "fight":
        print("What move will you use?")
        Move_Choice = input("Your Sableye knows: Scratch, Tackle, Psychic and Bite. ")
        
        if Move_Choice == "tackle":
            sleep(2)
            print("Sableye used Tackle!")
            sleep(2)
            Pikachu_Hp = int(Pikachu_Hp) - int(scratch)
            print("U did",tackle,"Damage!")
            sleep(2)
            print("Pikachu now has",Pikachu_Hp,"Hp")
            sleep(2)
            if Pikachu_Hp <=0:
                pikachu_dead = True
                if pikachu_dead == True:
                    print("You defeated Pikachu!")
                    quit()
        
        elif Move_Choice == "scratch":
            sleep(2)
            print("Sableye used scratch!")
            sleep(2)
            Pikachu_Hp = int(Pikachu_Hp) - int(scratch)
            print("U did",scratch,"Damage!")
            sleep(2)
            print("Pikachu now has",Pikachu_Hp,"Hp")
            sleep(2)
            if Pikachu_Hp <=0:
                pikachu_dead = True
                if pikachu_dead == True:
                    print("You defeated Pikachu!")
                    quit()
        
        elif Move_Choice == "psychic":
            sleep(2)
            print("Sableye used Psychic!")
            sleep(2)
            Pikachu_Hp = int(Pikachu_Hp) - int(psychic)
            print("You did",psychic,"Damage!")
            sleep(2)
            print("Pikachu now has",Pikachu_Hp,"Hp")
            sleep(2)
            if Pikachu_Hp <=0:
                pikachu_dead = True
                if pikachu_dead == True:
                    print("You defeated Pikachu!")
                    quit()

        elif Move_Choice == "bite":
            sleep(2)
            print("Sableye used Bite!")
            sleep(2)
            Pikachu_Hp = int(Pikachu_Hp) - int(bite)
            print("You did",bite,"Damage!")
            sleep(2)
            print("Pikachu now has",Pikachu_Hp,"Hp")
            sleep(2)
            if Pikachu_Hp <=0:
                pikachu_dead = True
                if pikachu_dead == True:
                    print("You defeated Pikachu!")
                    quit()

        
        print("It is now Pikachu's turn!")
        sleep(2)
        pikachu_move = random.randint(1,4)
        if pikachu_move == 1:
            sableye_Hp = int(sableye_Hp) - int(scratch)
            print("The Wild Pikachu used Scratch!")
            sleep(2)
            print("Sableye now has",sableye_Hp,"Hp")
            sleep(2)
            if sableye_Hp <=0:
                sableye_dead = True
                if sableye_dead == True:
                    print("You were defeated Pikachu!")
                    quit()

        if pikachu_move == 2:
            sableye_Hp = int(sableye_Hp) - int(thunderbolt)
            print("The Wild Pikachu used Thunderbolt!")
            sleep(2)
            print("Sableye now has",sableye_Hp,"Hp")
            sleep(2)
            if sableye_Hp <=0:
                sableye_dead = True
                if sableye_dead == True:
                    print("You were defeated Pikachu!")
                    quit()

        if pikachu_move == 3:
            sableye_Hp = int(sableye_Hp) - int(tackle)
            print("The Wild Pikachu used Tackle!")
            sleep(2)
            print("Sableye now has",sableye_Hp,"Hp")
            sleep(2)
            if sableye_Hp <=0:
                sableye_dead = True
                if sableye_dead == True:
                    print("You were defeated Pikachu!")
                    quit()


        if pikachu_move == 4:
            sableye_Hp = int(sableye_Hp) - int(bite)
            print("The Wild Pikachu used Bite!")
            sleep(2)
            print("Sableye now has",sableye_Hp,"Hp")
            sleep(2)
            if sableye_Hp <=0:
                sableye_dead = True
                if sableye_dead == True:
                    print("You were defeated Pikachu!")
                    quit()
        
        



    elif fightorflight == "run":
        sleep(2)
        run_chance = random.randint(1,4)
        if run_chance == 1:
            print("You escaped safely!")
            quit()
        else:
            print("You failed to run away!")
            sleep(2)
            print("It is now Pikachu's turn!")
            sleep(2)
        pikachu_move = random.randint(1,4)
        if pikachu_move == 1:
            sableye_Hp = int(sableye_Hp) - int(scratch)
            print("The Wild Pikachu used Scratch!")
            sleep(2)
            print("Sableye now has",sableye_Hp,"Hp")
            sleep(2)
            if sableye_Hp <=0:
                sableye_dead = True
                if sableye_dead == True:
                    print("You were defeated Pikachu!")
                    quit()
                    
        if pikachu_move == 2:
            sableye_Hp = int(sableye_Hp) - int(thunderbolt)
            print("The Wild Pikachu used Thunderbolt!")
            sleep(2)
            print("Sableye now has",sableye_Hp,"Hp")
            sleep(2)
            if sableye_Hp <=0:
                sableye_dead = True
                if sableye_dead == True:
                    print("You were defeated Pikachu!")
                    quit()

        if pikachu_move == 3:
            sableye_Hp = int(sableye_Hp) - int(tackle)
            print("The Wild Pikachu used Tackle!")
            sleep(2)
            print("Sableye now has",sableye_Hp,"Hp")
            sleep(2)
            if sableye_Hp <=0:
                sableye_dead = True
                if sableye_dead == True:
                    print("You were defeated Pikachu!")
                    quit()


        if pikachu_move == 4:
            sableye_Hp = int(sableye_Hp) - int(bite)
            print("The Wild Pikachu used Bite!")
            sleep(2)
            print("Sableye now has",sableye_Hp,"Hp")
            sleep(2)
            if sableye_Hp <=0:
                sableye_dead = True
                if sableye_dead == True:
                    print("You were defeated Pikachu!")
                    quit()

