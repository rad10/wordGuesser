#!/usr/bin/python3
from random import randint
from math import floor
maxRandRange = 20
word_dict = ['apple', 'fork', 'knife', 'sparrow', 'card', 'hard', 'dice', 'rice', 'well', 'smell']
word_dict_len = []
for i in word_dict:
    if (not len(i) in word_dict_len):
        word_dict_len.append(len(i))

#dict = word_dict

def getRandLength():
    while True:
        l = randint(2, 10)
        if l in word_dict_len:
            return l
def getRandWord(secLength, dictionary):
    l = int(secLength)

def RandWord(dictionary):
    return dictionary[randint(0, len(dictionary)-1)]

def randLower(): return chr(randint(97, 122))
def randUpper(): return chr(randint(65, 90))
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
def scrambleDict(secret, dtype):
    #l = len(secret)
    l = int(secret)
    numDict = []
    moldWord = ""
    dtype = str(dtype)
    table = ""
    if dtype[0] == 's': dtype = dtype[1:]
    if ('l' in dtype): table += "l"
    if ('u' in dtype): table += "u"
    if ('n' in dtype): table += "n"
    if ('s' in dtype): table += "s"
    for listSize in range(maxRandRange):
        for char in range(l):
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
    k = 4
    print("list of possible words:")
    l = len(easylist[0])
    s = 1
    printable = ""
    if (l <= 2): s = 6 * k
    elif (l <= 4): s = 4 * k
    elif (l <= 6): s = 3 * k
    elif (l <= 10): s = 2 * k
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
    elif (i==1):
        difficulty = str(input("choose difficulty (easy shows words that it could be; hard only tels you length of word) [easy/hard]: ")).lower()
        if(difficulty == "easy"):
            return True #printEasyList(easyList(secretWord, word_dict))
        elif(difficulty == "hard"):
            return False #print("length of secret word:", secretLength)
        else:
            print("Error: not a selectable difficulty: rerun and try again (im not that forgiving")
            return -1
    elif (i==2):
        print("what dictionaries do you want to use?")
        print("l\tlowercase words based on hardcoded dictionary of real words")
        print("c\tcapitalized words ^")
        print("u\tfull uppercased words ^")
        print("n\trandomized number based on secret random length")
        print('s [luns]\tdictionary of randomized words that contain letters from added categories')
        #print("t\timport dictionary from file in csv format")
        print("\nExample input \"select lists: l, u, c\"\n")
        return str(input("Select lists: ")).split(', ')
    return
def creatDictionary(secretl, keys):
    sl = int(secretl)
    temp = []
    stor = []
    if 'l' in keys:
        temp = lowerDict(sl)
        for i in temp: stor.append(i)
    if 'c' in keys:
        temp = capDict(sl)
        for i in temp: stor.append(i)
    if 'u' in keys:
        temp = upperDict(sl)
        for i in temp: stor.append(i)
    if 'n' in keys:
        temp = scrambleDict(sl, "sn")
        for i in temp: stor.append(i)
    for i in keys:
        if i[0] == 's':
            temp = scrambleDict(sl, i)
            for e in temp: stor.append(e)
    return stor




def main():
    pins = score = 0
    #secretWord = dict[randint(0, len(dict)-1)]
    secretLength = getRandLength() #len(secretWord)
    display(0)
    diff = display(1)
    dict = creatDictionary(secretLength, display(2))
    dict.sort()
    secretWord = RandWord(dict)
    print("Secret word length:", secretLength)
    if diff: printEasyList(dict)
    print()
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