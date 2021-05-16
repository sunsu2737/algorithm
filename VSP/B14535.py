import sys
line = sys.stdin.readline
case = 1
while True:
    cal = {'Jan': 0, 'Feb': 0, 'Mar': 0, 'Apr': 0, 'May': 0, 'Jun': 0,
           'Jul': 0, 'Aug': 0, 'Sep': 0, 'Oct': 0, 'Nov': 0, 'Dec': 0}
    N = int(line())
    if N == 0:
        break
    for i in range(1, N+1):
        A, B, C = line().split()
        if B == '01':
            cal['Jan'] += 1
        elif B == '02':
            cal['Feb'] += 1
        elif B == '03':
            cal['Mar'] += 1
        elif B == '04':
            cal['Apr'] += 1
        elif B == '05':
            cal['May'] += 1
        elif B == '06':
            cal['Jun'] += 1
        elif B == '07':
            cal['Jul'] += 1
        elif B == '08':
            cal['Aug'] += 1
        elif B == '09':
            cal['Sep'] += 1
        elif B == '10':
            cal['Oct'] += 1
        elif B == '11':
            cal['Nov'] += 1
        elif B == '12':
            cal['Dec'] += 1
    print('Case #{0}:'.format(case))
    for i in cal.keys():
        print('{0}:{1}'.format(i, cal[i]*'*'))
    case += 1
