# -*- coding: utf-8 -*
# bytes
# immutable sequenace of bytes

# byte literals
valBytes = b'some data'

print valBytes
print valBytes.split()

# encoading and decoding 
unicodeStr = "Vi er sσ" # declared unicode in first line ******
print unicodeStr
data = unicodeStr.decode('utf-8')
print data
