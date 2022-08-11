try:
    hours = input ('To calculate some milfs salary, how many hours does she work? ')
    rate = input ('Now, at what rate is she earning at? ')
    hoursI = float (hours)
    rateI = float (rate)
    pay = hoursI * rateI
except:
    print ('error, please enter proper numbers')