# Basic scalar built-in type
# 2. float  - IEEE-754 double precision 64 bit
#             53 bit binary precision, 16 to 16 bit of decimal precision.

print(3.125)
print(3e8)  # 3*(10^8) 
print(1.6e-4)   # 1.6/(10^4)

# float constructor
val = float(7.23)
print val

valStr = float("7.123")
print valStr

print float("nan")  #not a number

print float("inf")  #infinity

print float("-inf") #negative infinity

print 1 + 1.2 #int + float is promated to float
