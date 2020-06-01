'''
blank verse generator

blank verse is written in iambic pentameter, so each line must be
10 syllables long with alternating stressed and unstressed
syllables.

this blank verse generator takes a corpus text and generates a
markov chain-based poem in blank verse of length n lines.

it uses a mostly brute force algorithm, generating lines of a
random number of words (2-10) and then checking whether they
are in iambic pentameter. if they are, it prints the line;
otherwise it discards it and tries again.

1. Generate line
2. Check for
    - 10 syllables?
    - Alternating stressed/unstressed?
3. Print line

'''

import random
import time
import string
import markovify
from os.path import join
from pysle import isletool
from pysle import pronunciationtools

root = join(".", "files")
isleDict = isletool.LexicalTool(join(root, '/home/jay/Dropbox/19-20/PoetryGen/ISLEdict.txt'))

# Set your text corpus here
with open("/home/jay/Dropbox/19-20/PoetryGen/shelley.txt") as f:
    shelley = f.read()

with open("/home/jay/Dropbox/19-20/PoetryGen/mobydick.txt") as f:
    mobydick = f.read()

with open("/home/jay/Dropbox/19-20/PoetryGen/witchcraft.txt") as f:
    witch = f.read()

textModelShelley = markovify.Text(shelley, state_size=2)
textModelDick = markovify.Text(mobydick, state_size=2)
textModelWitch = markovify.Text(witch, state_size=2)

text_model = markovify.combine([ textModelShelley, textModelDick, textModelWitch ], [ 1, 1.5, 2 ])


# Generates a sentence x chars or less
def writeLine(numberOfLines):
    for i in range(numberOfLines):
        return(text_model.make_short_sentence(random.randint(35,45)))

# Returns sylliable and stress information
def syllWord(searchWord):
    lookupResults = isleDict.lookup(searchWord)
    firstEntry = lookupResults[0][0]
    firstSyllableList = firstEntry[0]
    firstSyllableList = ".".join([u" ".join(syllable)
        for syllable in firstSyllableList])
    firstStressList = firstEntry[1]
    #print(searchWord)
    #print(firstSyllableList)
    #print(firstStressList)
    return(firstSyllableList, firstStressList)

# Simple syllable count function
def countSyll(word):
    syllaCount = 1 
    sylla = str(syllWord(word))
    syllaCount += sylla.count(".")
    return syllaCount

# Returns True if the line is 10 syllables
def isTenSyll(line):
    line = line.split()
    lineSyll = 0
    for word in line:
        if word == " ":
            continue
        else:
            lineSyll += countSyll(word)
    if lineSyll == 10:
        return True
    else:
        return False

# Returns True if the line is iambic
def isIambic(line, syllablesPerWord):
    # fancy coding stuff here
  
    iambicGoal = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    iambicList = []
    stressedSyllas = []
    
    line = line.split()
    for word in line:
        syllList, stressList = syllWord(word)
        stressedSyllas.append(stressList)
    
    #print("stressedSyllas: " + str(stressedSyllas))
    #print("syllablesPerWord: " + str(syllablesPerWord))

    for index, syllable in enumerate(syllablesPerWord):
        if syllable == 1:
            if stressedSyllas[index] == [0]:
                iambicList.append(1)
            else:
                iambicList.append(0)
        elif syllable == 2:
            if stressedSyllas[index] == [0]:
                iambicList.append(1)
                iambicList.append(0)
            elif stressedSyllas[index] == [0,1]:
                iambicList.append(1)
                iambicList.append(1)
            elif stressedSyllas[index] == [1]:
                iambicList.append(0)
                iambicList.append(1)
            else:
                iambicList.append(0)
                iambicList.append(0)
        elif syllable == 3:
            if stressedSyllas[index] == [0]:
                iambicList.append(1)
                iambicList.append(0)
                iambicList.append(0)
            elif stressedSyllas[index] == [0,1]:
                iambicList.append(1)
                iambicList.append(1)
                iambicList.append(0)
            elif stressedSyllas[index] == [0,2]:
                iambicList.append(1)
                iambicList.append(0)
                iambicList.append(1)
            elif stressedSyllas[index] == [1]:
                iambicList.append(0)
                iambicList.append(1)
                iambicList.append(0)
            elif stressedSyllas[index] == [1,2]:
                iambicList.append(0)
                iambicList.append(1)
                iambicList.append(1)
            elif stressedSyllas[index] == [2]:
                iambicList.append(0)
                iambicList.append(0)
                iambicList.append(1)
            else:
                iambicList.append(0)
                iambicList.append(0)
                iambicList.append(0)
    ''' 
    print("Iambic list:")
    print(iambicList)
    '''
    if iambicList == iambicGoal:
        return True
    else:
        return False

'''
def isBlank(line):
    if (isTenSyll(line) == True) && (isIambic(line) == True):
        return True
'''

def writeBlankLine():
    blankLine = false
    while (blankLine == false):
        testLine = writeLine(1)



isGood = False
attemptCounter = 0
lineWritten = 0

while isGood == False:
    try:
        attemptCounter += 1
        if attemptCounter%(random.randint(75,135)) == 0:
            #print("Attempt: " + str(attemptCounter))
            print("")
        if attemptCounter == 300:
            break
    
        testLine = writeLine(1)
        testLineSanitized = testLine.translate(str.maketrans('', '', string.punctuation)) # strips punctuation
        syllablesPerWord = []
        
        for word in testLineSanitized.split():
            #print(word)
            syllablesPerWord.append(countSyll(word))
            #print("syllablesPerWord: " + str(syllablesPerWord))
        
        #print("syllablesPerWord: " + str(syllablesPerWord))
        
        #print(isIambic(testLineSanitized, syllablesPerWord))

        if (isTenSyll(testLineSanitized) == True):
            #print("Ten syllables:")
            print(testLine)
            with open('tenSyllLines.txt', 'a') as tenSyllLines:
                tenSyllLines.write(testLine + "\n")
                if random.randrange(7) == 0:
                    tenSyllLines.write("\n")
            if (isIambic(testLineSanitized, syllablesPerWord) == True):
                print("!!!!!!!!!!!!!!!!!!")
                
                with open('iambicLines.txt', 'a') as saveFile:
                    saveFile.write(testLine + "\n\n")
                continue

            else:
                #print("not Iambic")
                continue
        else:
            #print("not ten syllables")
            continue
    except:
        continue


