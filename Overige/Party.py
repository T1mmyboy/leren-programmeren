from asyncio import FastChildWatcher


gastheer = input("Wat is de naam van de Gastheer")
gasten = 6
gasten = int(gasten)
drank = False
chips = True
blacklist = "Tim" 

if not gastheer == blacklist and drank == True and gasten == 0 or not gastheer == blacklist and drank == True and gasten <=12 and gasten >=5 or not gastheer == blacklist and  gasten >= 5 and gasten <=12 and drank and chips:
    print("Start the party")
else:
    print("No party")
