# Prabhas Kumra
# Assignment #7
# CS-458
import re
import string
import random

filename = "Pride&Prejudice.txt"
PUNCT=re.compile("[!#$%&()*+,-./:;<=>?@[\]^_`{|}~123456789']")

# reading in the file and storing in an array
with open(filename) as f:
    data = f.readlines()

# for i in range(5):
#     print(data[i])

# converting letters to lowecase
for x in range(len(data)):
    data[x] = data[x].lower()
    data[x] = re.sub(PUNCT, " ", data[x])

KEYS = ['qwerstyuiopasdfghjklzxcvbnm']
keys = list(KEYS)
print(keys)
