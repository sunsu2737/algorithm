people=[]

file=open('data.txt','r')


a=file.readline()
while True:
    if a=='':
        break
    name,age,roll=a.split()
    people.append([name,age,roll])
    a=file.readline()

file.close()

while True:
    command=input('1.추가 2.삭제 3.출력 0.종료 ')


    if command=='1':
        name=input('이름: ')
        age=input('나이: ')
        roll=input('직책: ' )
        people.append([name,age,roll])


    elif command=='2':
        del_name=input('삭제할 이름: ')
        flag=0
        for i in range(len(people)):
            if people[i][0]==del_name:
                people.pop(i)
                print('삭제 되었습니다.')
                flag=1
                break
        if flag==0:
            print(del_name+'은(는) 없습니다')
        

    elif command=='3':
        print('이름'.rjust(5)+'나이'.rjust(5)+'직책'.rjust(5))
        for person in people:
            for data in person:
                print(data.rjust(5),end='')
            print()
    elif command=='0':
        break

file=open('data.txt','w')

for person in people:
    for data in person:
        file.write(data)
        file.write(' ')
    file.write('\n')
file.close()