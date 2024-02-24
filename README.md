# Targeted wordlist

Script to generate passwords when testing against auth sites of a brand or from a file. It uses l33tspeak (leetspeak) permutations and has the option to load from a wordlist file with (-f) flag.

type ` ./targetWordlist -h ` to see the documentation.

![image](https://github.com/Ego2509/targetWordlist/assets/29050030/5b39bae7-3df6-495a-a54a-5d1d4941d66b)


# Usage example

Example:

```zsh
./targetWordlist -b test -y 2018 -Y 2020 -s '.*+' -o test_1820
```
this should generate a file named test_1820 with all leetspeak permutations of `test`, followed by the following other permutations:

noun1=permutations of `test`=i

noun2=years=j

noun3=spaces=k

based on the letters referring to each noun, the program is able to generate these permutations: i, ij, ik, ijk, ikj.

# Install

Clone the repo and use the script on the folder. Works on both `bash` and `zsh`.

```zsh
git clone https://github.com/Ego2509/targetWordlist.git
cd targetWordlist
./targetWordlist
```

Make sure you have the complete barebone folder. The programs inside this folder are used to separate the functionality into smaller tasks.

```zsh
./barebone
├── genleeterspeak.py
├── shuffle-files.py
└── unique
```

`genleeterspeak.py` maps comon letter permutations to numbers and outputs them to stdout.

`shuffle-files.py` allows to generate noun permutations comming from files as shown in the example.

`unique` is an update to the uniq program that serves the purpose of deduplicate files without sorting them. This preserves the intended order of the noun permutations.

# Disclaimer

This program serves the sole purpose of generating passwords based on the knowledge gained from a brand in order to automate the pentesting process. The program just generates a small subset of probable passwords and it is up to you to decide what is the scope and reach of said set. There are many tools to make many sorts of passwords such as `crunch`, and many wordlists have decent password lists such as `seclists`. _Do not try to hack anyone without prior permission to do so._


