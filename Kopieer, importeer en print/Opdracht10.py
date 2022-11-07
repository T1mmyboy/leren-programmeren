from operator import index
from fruitmand import fruitmand
from operator import itemgetter
fruitmand = sorted(fruitmand, key=itemgetter("weight", "name"), reverse=True)
for x in range(len(fruitmand)):
    print("Een",fruitmand[x]["name"],"weegt" ,fruitmand[x]["weight"]/1000,"Kg")

