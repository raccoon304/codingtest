import sys 
input = sys.stdin.readline 

word = input()
words = set()
for i in range(len(word)):
    for j in range(i, len(word)):
        words.add(word[i:j+1].rstrip())


print(len(words)-1)