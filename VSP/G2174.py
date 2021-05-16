import sys
line=sys.stdin.readline
D={'E':(1,0),'W':(-1,0),'S':(0,-1),'N':(0,1)}
A,B=map(int,line().split())
class Robot:

    def __init__(self,name,x,y,d):
        self.name=name
        self.x=x
        self.y=y
        self.d=d

    def L(self):
        if(self.d=='N'):
            self.d='W'
        elif(self.d=='W'):
            self.d='S'
        elif(self.d=='S'):
            self.d='E'
        elif(self.d=='E'):
            self.d='N'
    def R(self):
        if (self.d == 'N'):
            self.d = 'E'
        elif (self.d == 'E'):
            self.d = 'S'
        elif (self.d == 'S'):
            self.d = 'W'
        elif (self.d == 'W'):
            self.d = 'N'
    def F(self):
        if (self.d == 'N'):
            self.x+=D['N'][0]
            self.y+=D['N'][1]
        elif (self.d == 'E'):
            self.x += D['E'][0]
            self.y += D['E'][1]
        elif (self.d == 'S'):
            self.x += D['S'][0]
            self.y += D['S'][1]
        elif (self.d == 'W'):
            self.x += D['W'][0]
            self.y += D['W'][1]
    def is_wall(self):
        if (self.x>A or self.y>B) or (self.x<1 or self.y<1):
            print('Robot',self.name,'crashes into the wall')
            exit(0)
    def is_crush(self,R):
        if self.x==R.x and self.y==R.y:
            print("Robot",self.name,"crashes into robot",R.name)
            exit(0)


N,M=map(int,line().split())
robots=[]
for i in range(N):
    x,y,d=line().split()
    temp=Robot(i+1,int(x),int(y),d)
    robots.append(temp)

for i in range(M):
    name,command,cnt=line().split()
    name=int(name)-1
    cnt=int(cnt)
    if command=='F':
        for i in range(cnt):
            robots[name].F()
            for j in robots:
                if j.name==name+1:
                    continue
                robots[name].is_crush(j)
            robots[name].is_wall()
    elif command=='L':
        for i in range(cnt):
            robots[name].L()
    elif command=='R':
        for i in range(cnt):
            robots[name].R()


print('OK')