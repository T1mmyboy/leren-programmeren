from operator import ge
from os import name
from tracemalloc import stop


Naam = input("Wat is uw naam? ").lower()
try:
    if Naam == "justin":
        raise NameError("Justin je bent niet welkom hier")
    Leeftijd = input("Wat is uw leeftijd? ").lower()
    Leeftijd = int(Leeftijd)
    if Leeftijd <= 16:
        print("U bent te jong voor deze baan!")
        quit()

    Geslacht = input("Wat is uw geslacht? ").lower()
    print("De vragen komen nu!")
    ervaring_dieren = input("Hoeveel jaar ervaring heeft u met dieren-dressuur? ").lower()
    ervaring_jongleren = input("Hoeveel jaar ervaring heeft u met jongleren? ").lower()
    ervaring_acrobatiek = input("Hoeveel jaar ervaring heeft u met acrobatiek? ").lower()
    diploma = input("Bent u in bezit van een MBO-4 Diploma? ").lower()
    rijbewijs = input("Bent u in bezit van een vrachtwagen rijbewijs? ").lower()
    hoed = input("Bent u in bezit van een hoge hoed? ").lower()
    if Geslacht == "man" :
        haar = input("Hoe breed is uw snor in cm? ").lower()
    elif Geslacht == "vrouw" :
        haar = input("Hoe lang is uw krulhaar? ").lower()
    lengte = input("Hoe lang bent u? ").lower()
    gewicht = input("Hoeveel weegt u? ").lower()
    certificaat = input("Heeft u het certificaat ""Overleven met gevaarlijk personeel").lower()
    randomvraag1 = input("Heeft u een clownsneus? ").lower()
    if randomvraag1 == "nee":
        print("U heeft een clownsneus nodig!")
        quit()
        
    randomvraag2 = input("Heeft u clownschoenen? ").lower()
    randomvraag3 = input ("Heeft u medische aandoeningen? ").lower()
    randomvraag4 = input("Hoeveel broers of zussen heeft u? ").lower()

    ervaring_dieren = int (ervaring_dieren)
    ervaring_acrobatiek = int (ervaring_acrobatiek)
    ervaring_jongleren = int (ervaring_jongleren)
    haar = int (haar)
    lengte = int (lengte)
    gewicht = int (gewicht)

    goed = False
    if ervaring_dieren >= 4 :    
        if diploma == "ja":
            if rijbewijs == "ja" :
                if hoed == "ja" :
                    if haar  == "10" or "20" :
                        if lengte  >= 150 :
                            if gewicht >= 90 :
                                if certificaat == "ja" :
                                    goed = True 
                                    if goed == True :
                                        print("",Naam, "u bent perfect voor deze baan! u krijgt binnenkort een mail")
    elif ervaring_jongleren >= 5 :
        if diploma == "ja":
            if rijbewijs == "ja" :
                if hoed == "ja" :
                    if haar  == "10" or "20" :
                        if lengte  >= 150 :
                            if gewicht >= 90 :
                                if certificaat == "ja" :
                                    goed = True 
                                    if goed == True :
                                        print("",Naam, "u bent perfect voor deze baan! u krijgt binnenkort een mail")
    elif ervaring_acrobatiek >= 3 :
        if diploma == "ja":
            if rijbewijs == "ja" :
                if hoed == "ja" :
                    if haar  == "10" or "20" :
                        if lengte  >= 150 :
                            if gewicht >= 90 :
                                if certificaat == "ja" :
                                    goed = True 
                                    if goed == True :
                                        print("",Naam, "u bent perfect voor deze baan! u krijgt binnenkort een mail")


    if goed == False :
        print ("Helaas",Naam, "bent u niet geschikt voor deze baan.")
except NameError: 
    print("Justin be gone")
    quit()