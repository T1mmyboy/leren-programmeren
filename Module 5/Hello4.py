from timeit import repeat
def NaamEnLeeftijd():
    namen={}
    repeat = True
    nummer = 0
    factor = 1
    while repeat == True:
        naam = input("Wat is uw naam : ").capitalize()
        if naam != "Stop":
                try:
                    leeftijd = int(input("Hoe oud bent u? : "))
                    if leeftijd != "Stop":
                        namen[naam] =leeftijd  
                    else:                            
                        break
                except:
                    print("Uw leeftijd moet een getal zijn!")
        else:
            return namen
NaamEnLeeftijd()
for key in NaamEnLeeftijd():
    print(key)



