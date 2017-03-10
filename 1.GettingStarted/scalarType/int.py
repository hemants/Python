# Basic scalar built-in type
# 1. int    - unlimited signed integer

print(10)       #decimal
print(0b10)     #binary
print(0o10)     #octo
print(0x10)     #hex

# int constructor
intVal = int(3.15)
print intVal

intValNeg = int(-6.1)
print intValNeg

intValStr = int("123")
print intValStr

intValbase2 = int("110", 2) # 1*(2^2) + 1*(2^1) + 0*(2^0) =  6
print intValbase2

intValbase3 = int("210", 3) # 2*(3^2) + 1*(3^1) + 0*(3^0) =  21
print intValbase3
