current_number = 0
previous_number = 0
for current_num in [0,1,2,3,4,5,6,7,8,9]:
    current_number = current_num
    previous_number = current_num - 1
    sum = current_number + previous_number
    print ('current number:', current_number, 'previous number:', previous_number, 'sum:', sum)