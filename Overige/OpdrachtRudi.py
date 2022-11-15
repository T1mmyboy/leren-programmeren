lijst = []
for x in range(3):
    nummer = int(input("Welk getal? "))
    lijst.append(nummer)
resultaat = list (filter (lambda x: (x % 3 == 0), lijst))
print(len(resultaat))
lijst.sort()
print (lijst[0],lijst[-1])