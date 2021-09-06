from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')
storyWords = []

for line in story:
    lineWords = line.decode('utf8').split()
    for word in lineWords:
            storyWords.append(word)

story.close()

# print(storyWords)

wordCounter = {}

for word in storyWords:
    if word in wordCounter:
        wordCounter[word] += 1
    else :
        wordCounter[word] = 1

print(wordCounter)