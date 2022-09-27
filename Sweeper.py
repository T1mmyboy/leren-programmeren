from random import randint

play = True
ronde = 1
ronde = int(ronde)
bomb = randint(1,10)
score_gebruiker = 0
score_gebruiker = int(score_gebruiker)

while play == True:
    antwoord_bomb = input("het is nu ronde "+str(ronde)+": Op welk getal denkt u dat de bom niet ligt? ")
    antwoord_bomb = int(antwoord_bomb)
    if bomb == antwoord_bomb:
        print("BOEM")
        print("Game Over")
        print("Uw score was:",score_gebruiker,"")
        quit()
    else:
        nextround = input("wilt u naar ronde "+str(ronde)+"? ja/nee? ").lower()
        if nextround == "ja":
            ronde = ronde+1
            play = True
            score_gebruiker = ronde * ronde
        else:
            print("Uw score was:",score_gebruiker,"")
            play = False

    pass
