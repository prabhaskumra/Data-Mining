# Prabhas Kumra
# Assignment #7
# CS-458

import re
import string
import copy
import random

def readFile():
    filename = "Pride&Prejudice.txt"

    # reading in the file and storing in an array
    with open(filename) as f:
        # data = f.readlines()
        data = f.read().splitlines()

    return data

def removePunct(data):
    PUNCT=re.compile("[!#$%&()*+,-./:;<=>?@[\]^_`{|}~123456789']")

    # removing linefeeds or empty data from the list
    cleanData = list() 
    for x in range(len(data)):
        if(len(data[x]) > 0):
            cleanData.append(data[x])       

    # converting letters to lowecase and removing Punctuation 
    for x in range(len(cleanData)):
        cleanData[x] = cleanData[x].lower()
        cleanData[x] = re.sub(PUNCT, " ", cleanData[x])

    # for x in range(10):
        # print(cleanData[x])   

    return cleanData

def buildKeys():

    KEYS = {  
		97 : {0 : 's', 1 : 'q', 2 : 'w'}, 
		98 : {0 : 'v', 1 : 'n', 2 : 'g'},
        99 : {0 : 'v', 1 : 'x', 2 : 'd'},
        100 : {0 : 's', 1 : 'f', 2 : 'e'},
        101 : {0 : 'w', 1 : 'r', 2 : 'd'},
        102 : {0 : 'd', 1 : 'g', 2 : 'r'},
        103 : {0 : 'f', 1 : 'h', 2 : 'b'},
        104 : {0 : 'j', 1 : 'g', 2 : 'f'},
        105 : {0 : 'k', 1 : 'u', 2 : 'o'},
        106 : {0 : 'h', 1 : 'k', 2 : 'u'},
        107 : {0 : 'j', 1 : 'l', 2 : 'i'},
        108 : {0 : 'o', 1 : 'k', 2 : 'j'},
        109 : {0 : 'n', 1 : 'b', 2 : 'j'},
        110 : {0 : 'b', 1 : 'm', 2 : 'j'},
        111 : {0 : 'p', 1 : 'i', 2 : 'l'},
        112 : {0 : 'o', 1 : 'i', 2 : 'l'},
        113 : {0 : 'w', 1 : 'a', 2 : 'e'},
        114 : {0 : 't', 1 : 'e', 2 : 'f'},
        115 : {0 : 'a', 1 : 'd', 2 : 'w'},
        116 : {0 : 'r', 1 : 'y', 2 : 'u'},
        117 : {0 : 'y', 1 : 'i', 2 : 'j'},
        118 : {0 : 'c', 1 : 'b', 2 : 'f'},
        119 : {0 : 'q', 1 : 'e', 2 : 's'},
        120 : {0 : 'z', 1 : 'c', 2 : 's'},
        121 : {0 : 't', 1 : 'u', 2 : 'h'},
        122 : {0 : 'a', 1 : 'x', 2 : 's'}
        } 

    return KEYS

def buildNoisyFile(data, KEYS):
    random.seed(20)

    for i in range(len(data)):
        splitted = data[i].split()
        # print(splitted)
        for j in range(len(splitted)):
            r = random.random()
            if r <= .10:
                word = (splitted[j])
                alphabet = word[random.randrange(len(word))]
                if alphabet.isalpha():
                    index = ord(alphabet)
                    word = re.sub(alphabet, KEYS[index] [random.randrange(2)], word)
                splitted[j] = word
        # print(splitted)
        data[i] = splitted

    return data

def main():
    data = readFile()
    data = removePunct(data)
    KEYS = buildKeys()
    
    originalData = copy.deepcopy(data)
    # making list of list of the data
    for i in range(len(originalData)):
        splitted = originalData[i].split()
        originalData[i] = splitted

    noisyFile = buildNoisyFile(data, KEYS)

    originalTraining = []
    noisyTraining = []
    originalTesting = []
    noisyTesting = []

    # splitting the data 
    for x in range(len(originalData)):
        if x < 423 :
            originalTesting.append(originalData[x]) 
            noisyTesting.append(noisyFile[x])
        else:
            originalTraining.append(originalData[x])
            noisyTraining.append(noisyFile[x])


    print((originalTesting[2][12]))
    print((originalTraining[2][12]))
    print((noisyTesting[2][12]))
    print((noisyTraining[2][12]))

if __name__ == "__main__":
    main()
