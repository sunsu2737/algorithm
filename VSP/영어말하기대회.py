def solution(word, score, speech: str):
    answer = 0
    dp = [0]*100001
    speech = speech.lower()
    for i in range(len(word)):
        word[i] = word[i].lower()
    if speech[0].isalpha():
        if speech[0] in word:
            dp[0] = score[word.index(speech[0])]
        else:
            dp[0] = 1

    for i in range(1, len(speech)):
        if speech[i].isalpha():
            dp[i] = dp[i-1]+1
            for j in range(i, i-10, -1):
                if j < 0:
                    break
                if speech[j:i+1] in word:
                    dp[i] = max(dp[i], dp[j-1] +
                                score[word.index(speech[j:i+1])])
        elif i == len(speech)-1:
            dp[i] = dp[i-1]
            for j in range(i, i-10, -1):
                if j < 0:
                    break
                if speech[j:i+1] in word:
                    dp[i] = max(dp[i], dp[j-1] +
                                score[word.index(speech[j:i+1])])
        else:
            dp[i] = dp[i-1]

    # print(dp[:len(speech)])

    return max(dp)


print(solution(["a", "a!", "c", "d", "e"], [1000, 1002, 1, 2, 3], "aa!"))
