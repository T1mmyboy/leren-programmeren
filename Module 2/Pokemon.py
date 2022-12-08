from itertools import repeat
from random import choice
from time import 
import math
import random

def intro():
    Naam = input("What is your name? ")
    print("Welcome",Naam,"to the world of Pokémon!")
    (3)
    print("Your Pokémon companion is called a Sableye.")
    (3)
    print("Sableye is a ghost/dark type Pokémon.")
    (3)
    print("So its only Weakness is fairy type attacks.")
    (3)
    print("Oh no! It looks like a wild Pikachu broke in!")
    (3)
    print("You should fight the Pikachu with your new Sableye!")
    (3)
    print("You can always try to run away from a fight, but it won't always work!")
    (3)

thunderbolt = int(90)
sableye_Hp = int(90)
Pikachu_Hp = int(80)
scratch = int(40)
tackle = int(40)
psychic= int(95)
bite = int(60)
pikachu_dead = False
sableye_dead = False
while pikachu_dead == False and sableye_dead == False:
    
    if Pikachu_Hp <=0:
        pikachu_dead = True
        
            print("You defeated Pikachu!")
            break
    fightorflight = input("What will you do? fight or run? ").lower
    if fightorflight == "fight":
        print("What move will you use?")
        Move_Choice = input("Your Sableye knows: Scratch, Tackle, Psychic and Bite. ")
        if Move_Choice == "tackle":
            
            print("Sableye used Tackle!")
            
            Pikachu_Hp = int(Pikachu_Hp) - int(scratch)
            print("U did",tackle,"Damage!")
            
            print("Pikachu now has",Pikachu_Hp,"Hp")
            
            if Pikachu_Hp <=0:
                pikachu_dead = True
                
                    print("You defeated Pikachu!")
                    
        
        elif Move_Choice == "scratch":
            
            print("Sableye used scratch!")
            
            Pikachu_Hp = Pikachu_Hp - scratch
            print("U did",scratch,"Damage!")
            
            print("Pikachu now has",Pikachu_Hp,"Hp")
            
            if Pikachu_Hp <=0:
                pikachu_dead = True
                
                print("You defeated Pikachu!")
                    
        
        elif Move_Choice == "psychic":
            
            print("Sableye used Psychic!")
            
            Pikachu_Hp = int(Pikachu_Hp) - int(psychic)
            print("You did",psychic,"Damage!")
            
            print("Pikachu now has",Pikachu_Hp,"Hp")
            
            if Pikachu_Hp <=0:
                pikachu_dead = True
                
                print("You defeated Pikachu!")
                

        elif Move_Choice == "bite":
            print("Sableye used Bite!")
            Pikachu_Hp = int(Pikachu_Hp) - int(bite)
            print("You did",bite,"Damage!")
            print("Pikachu now has",Pikachu_Hp,"Hp")
            
            if Pikachu_Hp <=0:
                pikachu_dead = True
                print("You defeated Pikachu!")
                
                    
        print("It is now Pikachu's turn!")
        
        pikachu_move = random.randint(1,4)
        if pikachu_move == 1:
            sableye_Hp = int(sableye_Hp) - int(scratch)
            print("The Wild Pikachu used Scratch!")
            
            print("Sableye now has",sableye_Hp,"Hp")
            
            if sableye_Hp <=0:
                sableye_dead = True
                if sableye_dead == True:
                    print("You were defeated Pikachu!")
                    break
        if pikachu_move == 2:
            sableye_Hp = int(sableye_Hp) - int(thunderbolt)
            print("The Wild Pikachu used Thunderbolt!")
            
            print("Sableye now has",sableye_Hp,"Hp")
            
            if sableye_Hp <=0:
                sableye_dead = True
            
                print("You were defeated Pikachu!")
                break
        if pikachu_move == 3:
            sableye_Hp = int(sableye_Hp) - int(tackle)
            print("The Wild Pikachu used Tackle!")
            
            print("Sableye now has",sableye_Hp,"Hp")
            
            if sableye_Hp <=0:
                sableye_dead = True
                print("You were defeated Pikachu!")
                break


        if pikachu_move == 4:
            sableye_Hp = int(sableye_Hp) - int(bite)
            print("The Wild Pikachu used Bite!")
            
            print("Sableye now has",sableye_Hp,"Hp")
            
            if sableye_Hp <=0:
                sableye_dead = True
                if sableye_dead == True:
                    print("You were defeated Pikachu!")
                    break
        
        



    elif fightorflight == "run":
        
        run_chance = random.randint(1,4)
        if run_chance == 1:
            print("You escaped safely!")
            break
        else:
            print("You failed to run away!")
            
            print("It is now Pikachu's turn!")
            
        pikachu_move = random.randint(1,4)
        if pikachu_move == 1:
            sableye_Hp = int(sableye_Hp) - int(scratch)
            print("The Wild Pikachu used Scratch!")
            
            print("Sableye now has",sableye_Hp,"Hp")
            
            if sableye_Hp <=0:
                sableye_dead = True
                if sableye_dead == True:
                    print("You were defeated Pikachu!")
                    break
                    
        if pikachu_move == :
            sableye_Hp = int(sableye_Hp) - int(thunderbolt)
            print("The Wild Pikachu used Thunderbolt!")
            
            print("Sableye now has",sableye_Hp,"Hp")
            
            if sableye_Hp <=0:
                sableye_dead = True
                if sableye_dead == True:
                    print("You were defeated Pikachu!")
                    break

        if pikachu_move == 3:
            sableye_Hp = int(sableye_Hp) - int(tackle)
            print("The Wild Pikachu used Tackle!")
            
            print("Sableye now has",sableye_Hp,"Hp")
            
            if sableye_Hp <=0:
                sableye_dead = True
                if sableye_dead == True:
                    print("You were defeated Pikachu!")
                    break


        if pikachu_move == 4:
            sableye_Hp = int(sableye_Hp) - int(bite)
            print("The Wild Pikachu used Bite!")
            
            print("Sableye now has",sableye_Hp,"Hp")
            
            if sableye_Hp <=0:
                sableye_dead = True
                if sableye_dead == True:
                    print("You were defeated Pikachu!")
                    break

