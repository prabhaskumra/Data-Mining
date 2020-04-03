# Prabhas Kumra
# Assignment #7
# CS-458
import re
import string

filename = "Pride&Prejudice.txt"

# reading in the file and storing in an array
with open(filename) as f:
    data = f.readlines()

# converting letters to lowecase
for x in range(len(data)):
    data[x] = data[x].lower()

# for i in range(5):
#     print(data[i])
print(string.punctuation)

print('!Hello.'.strip(string.punctuation))


foo = '!Hello.World!1!'
print(foo)
lulu = foo.strip(string.punctuation)
print(lulu)
