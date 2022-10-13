import __future__
word = input("Woord: ")
worda = word[::-1]
print(worda)
wordb = word
print(wordb+ " "+ wordb )
wordc = word
for i in wordc:
    for x in range(2):
       print(i, end= "")
print(worda +" " +wordb+ " "+i)

    
