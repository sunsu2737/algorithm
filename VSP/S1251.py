import sys
line = sys.stdin.readline

word = line().strip()

min_word = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'

for i in range(len(word)-2):
    for j in range(i+1, len(word)-1):
        if min_word > word[i::-1]+word[j:i:-1]+word[len(word):j:-1]:
            min_word = word[i::-1]+word[j:i:-1]+word[len(word):j:-1]
print(min_word)
