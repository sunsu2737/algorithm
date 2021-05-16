def solution(s):
    length = len(s)
    start = 0
    end = 1
    count = 1
    size = 1
    min_s = s
    cur_s = ''
    pre_word = ''
    while True:
        if pre_word == '':
            pre_word = s[start:end]
        else:
            if pre_word == s[start+size:end+size]:
                count += 1
                start += size
                end += size
            else:
                if count > 1:
                    cur_s += str(count)+pre_word
                    pre_word = ''
                    start += size
                    end += size
                    count = 1
                else:
                    cur_s += pre_word
                    pre_word = ''
                    start += size
                    end += size
        if end+size > length:
            if count > 1:
                cur_s += str(count)+pre_word
                pre_word = ''
                start += size
                end += size
                count = 1

            cur_s += s[start:]

            if len(cur_s) < len(min_s):
                min_s = cur_s
            cur_s = ''
            pre_word = ''
            size += 1
            start = 0
            end = start+size
        if size > length//2:
            break

    return len(min_s)