#Multiply numbers smaller than 1000 and add if they bigger than 1000
try:
    user_input = input ('Number one: ')
    user_input2 = input ('Number two: ')
    user_input = int (user_input)
    user_input2 = int (user_input2)
    sum = user_input * user_input2
    if sum > 1000:
        sum = user_input + user_input2
    print (sum)
except:
    print ('Error!! Please try again...')