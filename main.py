fileName = "words.txt"
writeFileName = "filteredWords.txt"

def HasDuplicateLetters(word):
    characterList = []
    for character in word:
        if not character in characterList:
            characterList.append(character)
        else:
            return True
    return False

def HasInvalidCharacters(word, invalidCharacters):
    for invalidCharacter in invalidCharacters:
        if invalidCharacter in word:
            return True
    return False

def HasCapitalLetters(word):
    return word.capitalize() == word



file = open(fileName,"r")
wordList = []
invalidCharacterList = ['\'']
for line in file:
    lineLength = len(line)
    if lineLength == 6 and not HasDuplicateLetters(line) and not HasInvalidCharacters(line, invalidCharacterList) and not HasCapitalLetters(line):
        wordList.append(line)
print(wordList)
file.close()
file = open(writeFileName, 'w')
for word in wordList:
    file.write(word)