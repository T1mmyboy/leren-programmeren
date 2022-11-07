from fruitmand import fruitmand
kleuren = []
fruitmand.pop(4)
for x in range(len(fruitmand)):
    if fruitmand[x]["color"] not in kleuren:
        kleuren.append(fruitmand[x]["color"])
print(kleuren)