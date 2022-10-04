# name of student: Tim
# number of student: 99074833
# purpose of program: to tell you how much change you have to give back
# function of program: it asks u how many u need to pay and how many u paid, then it asks in what coins u want to pay, after it shows what coins u paid with.
# structure of program: first inputs, then math, then it prints

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #
vijfeuro = 0
tweeeuro = 0
drieeuro = 0
vijftigcent = 0
twintig = 0
tiencent = 0
vijfcent = 0
tweecent = 0
eencent = 0

if change > 0: #
  coinValue = 500 #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #
      if coinValue == 500:
        vijfeuro = vijfeuro +1 * nrCoinsReturned
      elif coinValue == 300:
        drieeuro = drieeuro +1 * nrCoinsReturned
      elif coinValue == 200:
        tweeeuro = tweeeuro +1 * nrCoinsReturned
      elif coinValue == 50:
        vijftigcent = vijftigcent+1 * nrCoinsReturned
      elif coinValue == 20:
        twintig = twintig +1 * nrCoinsReturned
      elif coinValue == 10:
        tiencent = tiencent +1 * nrCoinsReturned
      elif coinValue == 5:
        vijfcent = vijfcent +1 * nrCoinsReturned
      elif coinValue == 2:
        tweecent = tweecent+1 *  nrCoinsReturned
      elif coinValue == 1:
        eencent = eencent +1 * nrCoinsReturned
      

# comment on code below: 
    
    
    if coinValue == 500:
      coinValue =300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #
  print('You need to give back ', str(change) + ' cents')


else:
  print('done')
print("U heeft",nrCoinsReturned,"teruggegeven, waarvan",vijfeuro,"5 euro munten,",drieeuro,"3 euro munten,",tweeeuro,"2 euro munten,",vijftigcent,"50 cent munten,",twintig,"20 cent munten,",tiencent,"10 cent munten",vijfcent,"5 cent munten,",tweecent,"2 cent munten en",eencent,"1 cent munten" )