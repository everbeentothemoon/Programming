def method ():
    if hoursI > 40:
        regular = hoursI * rateI
        overtime = (hoursI - 40) + (rateI * 0.5)
        otp = overtime + regular
        print (otp)
    else:
        pay = hoursI * rateI
        print (pay)

hours = input ('How many hours did the slave work? ')
rate = input ('At what rate did the slave work? ')
hoursI = int (hours)
rateI = int (rate)
method ()
me = method ()
print ('The new wage with/without overtime rate is: ')

