# Basic scalar built-in type
# 4. bool   - boolean logical value

print True
print False

# bool constructr
# 0 is consider true value and all other are False
print "bool constructr from numeric values"
print bool(0)
print bool(0.0)
print bool(1)
print bool(-1)
print bool(-1.12)

# only expty string are considered as false value ***
print "bool constructr from string values"
print bool("True")  # o/p - True
print bool("False") # o/p - True ******
print bool("")      # o/p = false

# only empty is false
print "bool constructr from list values"
print bool([])  # o/p - false
print bool([1,2])   # o/p - true
