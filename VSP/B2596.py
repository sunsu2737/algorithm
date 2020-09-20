N=int(input())
word=input()
words=[]

for i in range(N):
    if word[0+i*6:6+6*i]=='000000' or word[0+i*6:6+6*i]=='100000' or word[0+i*6:6+6*i]=='010000' or word[0+i*6:6+6*i]=='001000' or word[0+i*6:6+6*i]=='000100' or word[0+i*6:6+6*i]=='000010' or word[0+i*6:6+6*i]=='000001':
        words.append('A')
    elif word[0+i*6:6+6*i]=='001111' or word[0+i*6:6+6*i]=='101111' or word[0+i*6:6+6*i]=='011111' or word[0+i*6:6+6*i]=='000111' or word[0+i*6:6+6*i]=='001011' or word[0+i*6:6+6*i]=='001101' or word[0+i*6:6+6*i]=='001110':
        words.append('B')
    elif word[0+i*6:6+6*i]=='010011' or word[0+i*6:6+6*i]=='110011' or word[0+i*6:6+6*i]=='000011' or word[0+i*6:6+6*i]=='011011' or word[0+i*6:6+6*i]=='010111' or word[0+i*6:6+6*i]=='010001' or word[0+i*6:6+6*i]=='010010':
        words.append('C')
    elif word[0+i*6:6+6*i]=='011100' or word[0+i*6:6+6*i]=='111100' or word[0+i*6:6+6*i]=='001100' or word[0+i*6:6+6*i]=='010100' or word[0+i*6:6+6*i]=='011000' or word[0+i*6:6+6*i]=='011110' or word[0+i*6:6+6*i]=='011101':
        words.append('D')
    elif word[0+i*6:6+6*i]=='100110' or word[0+i*6:6+6*i]=='000110' or word[0+i*6:6+6*i]=='110110' or word[0+i*6:6+6*i]=='101110' or word[0+i*6:6+6*i]=='100010' or word[0+i*6:6+6*i]=='100100' or word[0+i*6:6+6*i]=='100111':
        words.append('E')
    elif word[0+i*6:6+6*i]=='101001' or word[0+i*6:6+6*i]=='001001' or word[0+i*6:6+6*i]=='111001' or word[0+i*6:6+6*i]=='100001' or word[0+i*6:6+6*i]=='101101' or word[0+i*6:6+6*i]=='101011' or word[0+i*6:6+6*i]=='101000':
        words.append('F')
    elif word[0+i*6:6+6*i]=='110101' or word[0+i*6:6+6*i]=='010101' or word[0+i*6:6+6*i]=='100101' or word[0+i*6:6+6*i]=='111101' or word[0+i*6:6+6*i]=='110001' or word[0+i*6:6+6*i]=='110111' or word[0+i*6:6+6*i]=='110100':
        words.append('G')
    elif word[0+i*6:6+6*i]=='111010' or word[0+i*6:6+6*i]=='011010' or word[0+i*6:6+6*i]=='101010' or word[0+i*6:6+6*i]=='110010' or word[0+i*6:6+6*i]=='111110' or word[0+i*6:6+6*i]=='111000' or word[0+i*6:6+6*i]=='111011':
        words.append('H')
    else:
        print(i+1)
        exit(0)
print(''.join(words))