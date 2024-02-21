#!/bin/python
import sys
import os

#file input

ifs=[]

for i, arg in enumerate(sys.argv[1:]):
    ifs.append(arg)

#string extraction
#nouns=[noun1,noun2...]
nouns=[]
for filename in ifs:
    with open(filename,'r') as f:
        temp2=f.read().splitlines()
        nouns.append(temp2)

#[debug] 
print(nouns)

#this is the permutation pattern that will be generated:
#nouns[j][k]
#nouns[k][j]

with open("shuffled","a") as f:
    for i in nouns[0]:
        for j in nouns[1]:
            for k in nouns[2]:
                f.write(i+j+k+"\n")
                f.write(i+k+j+"\n")
