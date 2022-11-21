from timeit import repeat
def NaamEnLeeftijd():
    namen=[]
    leeftijden = []
    repeat = True
    nummer = 0
    factor = 1
    while repeat == True:
        naam = input("Wat is uw naam : ").capitalize()
        if naam != "Stop":
                try:
                    leeftijd = int(input("Hoe oud bent u? : "))
                    if leeftijd != "Stop":
                        namen.append(naam)
                        leeftijden.append(str(leeftijd))
                        continue
                    else:
                        for x in range(len(namen)):
                            print("",namen[x],"is",leeftijden[x],"Jaar")
                            x=x+1
                            break
                except:
                    print("Uw leeftijd moet een getal zijn!")
        else:
            print(namen) 
            for x in range(len(namen)):
                print("",namen[x],"is",leeftijden[x],"Jaar")
                x=x+1
            break
NaamEnLeeftijd()

