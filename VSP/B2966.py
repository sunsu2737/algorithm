Adrian = 'ABC'
Bruno = 'BABC'
Goran = 'CCAABB'
score = [0, 0, 0]
n = int(input())
answer = list(input())
'AAAABBBBCCCC'
'ABCABC'
for i, a in enumerate(answer):
    if Goran[i % 6] == a:
        score[2] += 1
    if Bruno[i % 4] == a:
        score[1] += 1
    if Adrian[i % 3] == a:
        score[0] += 1


maxs = max(score)
idxs = []
for i, v in enumerate(score):
    if maxs == v:
        idxs.append(i)
print(maxs)

for max_idx in idxs:
    if max_idx == 0:

        print('Adrian')
    elif max_idx == 1:

        print('Bruno')
    elif max_idx == 2:

        print('Goran')
