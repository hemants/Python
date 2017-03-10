# String
# str: immutable sequences of Unicode character\codepoints

print "it's a good thing"
print 'Good "thing"'

# escape sequeance
print 'it\'s a good thing.'

# raw string
path = r'c:\users\hemant\documents'
print path

# new line character
print "it's a good thing. \n What !! "

# multiline String
print """ This is a 
 multiline
    string"""

# str constructor
val = str(123)
print val
print val[0]

print type(val[1])

# immutable nature
strval = "hemant"
print strval.capitalize()
print strval

# Unicode
print '\345'
print '\xe5'
# print 'Vi er s\u00e5' #does not work  ... may be python 3