def solution(phone_book):
    minlen = 20
    min_book = []
    for i in range(len(phone_book)):
        if len(phone_book[i]) < minlen:
            minlen = len(phone_book[i])
    for i in range(len(phone_book)):
        if len(phone_book[i]) == minlen:
            min_book.append(phone_book[i])
            phone_book[i] = '0'
        phone_book[i] = phone_book[i][:minlen]
    print(phone_book)
    print(min_book)
    for i in range(len(min_book)):
        for j in range(len(phone_book)):
            if min_book[i] == phone_book[j]:
                return False

    return True
