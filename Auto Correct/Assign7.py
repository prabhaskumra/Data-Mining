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
    KEYS = ['qwerstyuiopasdfghjklzxcvbnm']
    keys = list(KEYS)

    a = ['s','q','w']
    b = ['v','n','g']
    c = ['v','x','d']
    d = []
    e = []
    f = []
    g = []
    h = []
    i = []
    j = []
    k = []
    l = []
    m = []
    n = []
    o = []
    p = []
    q = []
    r = []
    s = []
    t = []
    u = []
    v = []
    w = []
    x = []
    y = []
    z = []



    print(a[2])
    print(z)

def main():
    data = readFile()
    removePunct(data)
    buildKeys()

if __name__ == "__main__":
    main()
