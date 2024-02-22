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
