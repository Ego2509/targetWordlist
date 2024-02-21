#!/bin/python
import sys

shtext=[]

for i, arg in enumerate(sys.argv[1:]):
    shtext.append(arg)

#[debug] print(f"input {shtext}")

#letters mapped to numbers:
letters1="iIeEaAsSbBtToO"
netters1='11334455887700'

#letters mapped to numbers:
letters2="iIeEaAsSbBtToO"
netters2='1133@@$$667700'

map_1=dict(zip(letters1,netters1))
map_2=dict(zip(letters2,netters2))
#[debug] print(map_)

def generate_wl(word:str,map_:dict,letters,netters):
    placeholders=[]
    for i,l in enumerate(word):
        if l in letters:
            placeholders.append(i)

    # len(placeholders) is what defines permutations needed
    # len(perms)=2**len(placeholders)
    pl=len(placeholders)
    permslen=2**pl
    #[debug] print(f"permslen{permslen}")
    perms=[bin(i)[2:].zfill(pl) for i in range (0,permslen)]
    #[debug] print(f"perms{perms}")
    ph=[]
    for p in perms:
        x=[]
        for i,b in enumerate(p):
            if int(b): x.append(placeholders[i])
        #[debug] print(f"x{x}")
        ph.append(x)
    #[debug] print(f"ph{ph}")

    generated=[]
    for j in ph:
        new_word=list(word)
        for jj in j:
            new_word[jj]=map_[word[jj]]
        new_word_x="".join(new_word)
        generated.append(new_word_x)

    print(word.title())
    print(word.upper())
    [print(g.title()) for g in generated]
    [print(g) for g in generated]
    [print(g.upper()) for g in generated]
    # this has to be cleaned up (deduplicated/filtered)
    # with unique (custom bash)

[generate_wl(x,map_2,letters2,netters2) for x in shtext]
#[debug] [generate_wl(x,map_1,letters1,netters1) for x in shtext]

