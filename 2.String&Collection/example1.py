# python 3
from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as response:
    #print(type(response))
    story_words = []
    for line in response:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

# observe story_words is still in scope
print(story_words)