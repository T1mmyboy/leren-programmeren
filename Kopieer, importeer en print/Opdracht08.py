from fruitmand import fruitmand
totaal = 0
watermeloen = {
    "name" : "watermeloen",
    "weight" : 3500,
    "color" : "green",
    "round" : False}
fruitmand.append(watermeloen)
for x in range(len(fruitmand)):
    totaal = totaal + fruitmand[x]["weight"]
print(totaal)