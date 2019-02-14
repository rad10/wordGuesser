#!/usr/bin/python3.6
from random import randint
from math import floor
maxRandRange = 20
word_dict = ['apple', 'fork', 'knife', 'sparrow', 'card', 'hard', 'dice', 'rice', 'well', 'smell', 'orange', 'laptop', 'window', 'bus', 'robot','keys','cable','roof','chair','loud','eat','diet', 'mat',' cat','rat','fat','hall','mall','stall','child','mild','tall','small','fall','car','can','tin','iron','ramp','swing','children','fantasy','fact','act','read','need','wimper','style','class','family','character','java','python','c++']
dict = word_dict

def randLower(): return repr(97, 122)
def randUpper(): return repr(65, 90)
def randNum(): return randint(0,9)
def randSym():
    sym = ['!', '\"', '\'', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '_', '=', '[', ']', '\\', ';', ':', '/', '?', ',', '.', '<', '>', '~', '@']
    return sym[randint(0, len(sym)-1)]
#Dictionary generators
def lowerDict(secret): #secretLength
    useDict = []
    for i in word_dict:
        if (len(i) == secret): useDict.append(str(i).lower())
    return useDict
def capDict(secret):
    useDict = []
    for i in word_dict:
        if (len(i) == secret): useDict.append(str(i).capitalize())
    return useDict
def upperDict(secret):
    useDict = []
    for i in word_dict:
        if (len(i) == secret): useDict.append(str(i).upper())
    return useDict
def scrambleNumDict(secret, dtype):
    #l = len(secret)
    l = int(secret)
    numDict = []
    moldWord = ""
    dtype = str(dtype)
    '''if (dtype == "n"): #random numberlist
        for listSize in range(maxRandRange):
            numDict.append(str(randint((10**(l-1)), (10**l)-1)))
        return numDict
    elif (dtype == "l"): #random all lowercase letters
        for listSize in range(maxRandRange):
            for char in range(secret): moldWord += repr(randint(97, 122))
            numDict.append(moldWord)
            moldWord = ""
        return numDict
    elif (dtype == "u"): #random all uppercase letters
        for listSize in range(maxRandRange):
            for char in range(secret): moldWord += randUpper()
            numDict.append(moldWord)
            moldWord = ""
        return numDict'''
    table = ""
    if True:
        if ('l' in dtype): table += "l"
        if ('u' in dtype): table += "u"
        if ('n' in dtype): table += "n"
        if ('s' in dtype): table += "s"
        for listSize in range(maxRandRange):
            for char in range(secret):
                t = table[randint(0, len(table)-1)]
                if (t == "l"): moldWord += randLower()
                elif(t == "u"): moldWord += randUpper()
                elif(t == "n"): moldWord += str(randNum())
                elif(t == "s" ): moldWord += randSym()
            numDict.append(moldWord)
            moldWord = ""
        return numDict
def getPins(secret, applied):
    c = 0
    if (len(secret) <= len(applied)):
        for i in range(len(secret)):
            if (secret[i] == applied[i]):
                c+=1
    elif (len(secret) > len(applied)):
        for i in range(len(applied)):
            if (secret[i] == applied[i]):
                c+=1
    return c
def easyList(secret, dictionary):
    easylist = []
    secret = str(secret)
    for i in dictionary:
        if (len(i) == len(secret)):
            easylist.append(i)
    easylist.sort()
    return easylist
def printEasyList(easylist):
    print("list of possible words:")
    l = len(easylist[0])
    s = 1
    printable = ""
    if (l <= 2): s = 6
    elif (l <= 4): s = 4
    elif (l <= 6): s = 3
    elif (l <= 10): s = 2
    else:
        for i in easylist:
            print(i)
        print()
        return
    print("debug:", int(len(easylist)/s))
    for y in range(0, int(len(easylist)/s)+1):
        for x in range(s):
            if(y*s+x < len(easylist)):
                printable += easylist[y*s + x] + "  "
        print(printable)
        printable = ""    
    return
def display(i):
    if (i==0): print("Welcome to the word guessing game.")
    return
#def creatDictionary(keys):

def main():
    pins = score = 0
    secretWord = dict[randint(0, len(dict)-1)]
    secretLength = len(secretWord)
    display(0)
    difficulty = str(input("choose difficulty (easy shows words that it could be; hard only tels you length of word) [easy/hard]: ")).lower()
    if(difficulty == "easy"):
        printEasyList(easyList(secretWord, word_dict))
    elif(difficulty == "hard"):
        print("length of secret word:", secretLength)
    else:
        print("Error: not a selectable difficulty: rerun and try again (im not that forgiving")
        return
    userWord = str(input("check word: "))
    pins = getPins(secretWord, userWord)
    while (pins != secretLength):
        print("pins accessed:", pins)
        score+=1
        print("currentScore:", score)
        userWord = str(input("check word: "))
        if (userWord == "giveUp"): break
        pins = getPins(secretWord, userWord)
    if (userWord == "giveUp"): print("correct answer:", secretWord)
    else: print("Correct! secret word:", secretWord)
    print("Score:", score)
    return
contin = True
while contin:
    main()
    contin = "true" == str(input("run again? [true/false]: ")).lower()
print("Thank you for playing!")