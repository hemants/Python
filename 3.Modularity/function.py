# python function

def square(x):
    if x==1:
        return
    return x*x

print(square(5)) # o/p: 25

rtnVal = square(1)
print(rtnVal) # o/p: None

print(rtnVal is None) # o/p: true

import words
words.fetch_words()