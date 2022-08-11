str = 'X-DSPAM-Confidence: 0.8475'
strI = str.find (' ')
print (strI)
line = str.find ('5', strI)
print (line)
host = str [strI + 1 : line + 2]
print (host)
hostI = float (host)
print (hostI)