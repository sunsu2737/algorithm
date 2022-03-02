n = int(input())
def counting_star(count):

    if count == 1:
        return ["*"]

    counting = counting_star(count//3)
    star  = []

    for c in counting:
        star.append(c * 3)
    for c in counting:
        star.append(c + ' '*(count//3) + c)
    for c in counting:
        star.append(c*3)

    return star

print('\n'.join(counting_star(n)))
    
