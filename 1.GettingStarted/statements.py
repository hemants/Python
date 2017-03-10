# Control flow structure
# 1. Conditional statement

print "# 1. Conditional statement"
if True:
    print "Output is true"

# if else statement 
val1 = 10
val2 = 20
if val1 != val2:
    print "true"
else:
    print "false"

#if elif block
val3 = 30
if val1 == val2:
    print "first true block"
elif val1 == val3:
    print "second true block"
else:
    print "else block"


# 2. While loop
print "# 2. While loop"
value = 0
while value <= 5:
    print value
    value += 1

value = 22
while True:
    if value == 19:
        break
    print value
    value -= 1

# 3. For loop
print "# 3. For loop"

dictobj =  {'key1': 'value1', 'key2': 'value2'}

for key in dictobj:
    print dictobj[key]