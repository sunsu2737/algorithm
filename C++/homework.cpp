#include<iostream>
#include<queue>
#include<vector>
#include<string>
using namespace std;

int N;
int board[100][100];

void run(queue<vector<int> > start){
    
    queue<vector<int > > next ;
    while(!start.empty()){
        
        int c=start.front().back();
        start.front().pop_back();
        int z=start.front().back();
        start.front().pop_back();
        int y=start.front().back();
        start.front().pop_back();
        int x=start.front().back();
        start.front().pop_back();
        start.pop();

        if(x==N-1 && y==N-1){
            cout<<"YES";
            exit(0);
        }
        
        
        if(c>0 && board[x][y]==2){
            continue;
        }
        
        if (0 <= x + 1 && x + 1 < N && 0 <= y && y < N && board[x + 1][y] != 1 && z==0)

            next.push({x+1,y,z,c+1});
        else if (z==0){
            board[x][y]=2;
            if (0 <= x && x < N && 0 <= y + 1 && y + 1 < N && board[x][y + 1] != 1 )
                next.push({x,y+1,1,c+1});
            if (0 <= x - 1 && x - 1 < N && 0 <= y && y < N && board[x - 1][y] != 1)
                next.push({x-1, y, 2,c+1});
            if (0 <= x && x < N && 0 <= y - 1 && y - 1 < N && board[x][y - 1] != 1)
                next.push({x, y-1, 3,c+1});
        }


        if (0 <= x  && x  < N && 0 <= y+1 && y+1 < N && board[x ][y+1] != 1 && z==1)

            next.push({x,y+1,z,c+1});
        else if (z==1){
            board[x][y]=2;
            if (0 <= x+1 && x+1 < N && 0 <= y  && y  < N && board[x+1][y ] != 1 )
                next.push({x+1,y,0,c+1});
            if (0 <= x - 1 && x - 1 < N && 0 <= y && y < N && board[x - 1][y] != 1)
                next.push({x-1, y, 2,c+1});
            if (0 <= x && x < N && 0 <= y - 1 && y - 1 < N && board[x][y - 1] != 1)
                next.push({x, y-1, 3,c+1});
        }


        if (0 <= x - 1 && x - 1 < N && 0 <= y && y < N && board[x - 1][y] != 1 && z==2)

            next.push({x-1,y,z,c+1});
        else if (z==2){
            board[x][y]=2;
            if (0 <= x && x < N && 0 <= y + 1 && y + 1 < N && board[x][y + 1] != 1 )
                next.push({x,y+1,1,c+1});
            if (0 <= x+1 && x+1 < N && 0 <= y  && y  < N && board[x+1][y ] != 1 )
                next.push({x+1,y,0,c+1});
            if (0 <= x && x < N && 0 <= y - 1 && y - 1 < N && board[x][y - 1] != 1)
                next.push({x, y-1, 3,c+1});
        }

        if (0 <= x  && x  < N && 0 <= y-1 && y-1 < N && board[x ][y-1] != 1 && z==3)

            next.push({x,y-1,z,c+1});
        else if (z==3){
            board[x][y]=2;
            if (0 <= x && x < N && 0 <= y + 1 && y + 1 < N && board[x][y + 1] != 1 )
                next.push({x,y+1,1,c+1});
            if (0 <= x - 1 && x - 1 < N && 0 <= y && y < N && board[x - 1][y] != 1)
                next.push({x-1, y, 2,c+1});
            if (0 <= x+1 && x+1 < N && 0 <= y  && y  < N && board[x+1][y ] != 1 )
                next.push({x+1,y,0,c+1});
        }
    if (!next.empty())
        
        run(next);
    }
}

int main(){
    cin>>N;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin>>board[i][j];
        }
    }
    board[0][0]=2;
    queue<vector<int> > Q;
    Q.push({0,0,0,0});
    Q.push({0,0,1,0});
    run(Q);
    cout<<"NO";
}