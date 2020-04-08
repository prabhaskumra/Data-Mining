# Prabhas Kumra
# Assignment #7
# CS-458

import re
import string
import random


def readFile():
    filename = "Pride&Prejudice.txt"

    # reading in the file and storing in an array
    with open(filename) as f:
        data = f.readlines()

    return data

def removePunct(data):
    PUNCT=re.compile("[!#$%&()*+,-./:;<=>?@[\]^_`{|}~123456789']")

    # converting letters to lowecase and removing Punctuation 
    for x in range(len(data)):
        data[x] = data[x].lower()
        data[x] = re.sub(PUNCT, " ", data[x])

    # for i in range(5):
    #     print(data[i])

def buildKeys():

    KEYS = {  
		'a' : {0 : 's', 1 : 'q', 2 : 'w'}, 
		'b' : {0 : 'v', 1 : 'n', 2 : 'g'},
        'c' : {0 : 'v', 1 : 'x', 2 : 'd'},
        'd' : {0 : 's', 1 : 'f', 2 : 'e'},
        'e' : {0 : 'w', 1 : 'r', 2 : 'd'},
        'f' : {0 : 'd', 1 : 'g', 2 : 'r'},
        'g' : {0 : 'f', 1 : 'h', 2 : 'b'},
        'h' : {0 : 'j', 1 : 'g', 2 : 'f'},
        'i' : {0 : 'k', 1 : 'u', 2 : 'o'},
        'j' : {0 : 'h', 1 : 'k', 2 : 'u'},
        'k' : {0 : 'j', 1 : 'l', 2 : 'i'},
        'l' : {0 : 'o', 1 : 'k', 2 : 'j'},
        'm' : {0 : 'n', 1 : 'b', 2 : 'j'},
        'n' : {0 : 'b', 1 : 'm', 2 : 'j'},
        'o' : {0 : 'p', 1 : 'i', 2 : 'l'},
        'p' : {0 : 'o', 1 : 'i', 2 : 'l'},
        'q' : {0 : 'w', 1 : 'a', 2 : 'e'},
        'r' : {0 : 't', 1 : 'e', 2 : 'f'},
        's' : {0 : 'a', 1 : 'd', 2 : 'w'},
        't' : {0 : 'r', 1 : 'y', 2 : 'u'},
        'u' : {0 : 'y', 1 : 'i', 2 : 'j'},
        'v' : {0 : 'c', 1 : 'b', 2 : 'f'},
        'w' : {0 : 'q', 1 : 'e', 2 : 's'},
        'x' : {0 : 'z', 1 : 'c', 2 : 's'},
        'y' : {0 : 't', 1 : 'u', 2 : 'h'},
        'z' : {0 : 'a', 1 : 'x', 2 : 's'}
        } 

    return KEYS

def buildNoisyFile():
    # random.seed(3)
    r = random.random()
    print(r)

def main():
    data = readFile()
    removePunct(data)
    KEYS = buildKeys()
    # print(KEYS)

    buildNoisyFile()

if __name__ == "__main__":
    main()
