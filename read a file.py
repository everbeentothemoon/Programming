file = input ('Enter the file name: ')
file = file.capitalize ()
ffile = open (file)
for me in ffile:
    print (me)