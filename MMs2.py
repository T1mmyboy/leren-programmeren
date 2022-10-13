from random import randint
MMs = {
1 : "Rood",
2 : "Blauw",
3 : "Groen",
4 : "Geel",
5 : "Bruin"
}
zak = []
try:
    aantal = input("Hoeveel M&Ms wilt u? : ")
    aantal = int(aantal)
    if aantal >100:
        quit()
    for x in range(aantal):
        getal = randint(1,5)
        zak.append(MMs[getal])
    print("Uw zak M&Ms :",zak)
except:
    print("Stop")
    quit()