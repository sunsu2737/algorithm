n=int(input())

for i in range(n,0,-1):

    if i==1:
        print('''1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.''')
    elif i==2:
        print('''2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.''')
    else:
        print('''%d bottles of beer on the wall, %d bottles of beer.
Take one down and pass it around, %d bottles of beer on the wall.'''%(i,i,i-1))
    print()
    
if n>1:
    print('''No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, %d bottles of beer on the wall.'''%n)
else:
    print('''No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, %d bottle of beer on the wall.'''%n)