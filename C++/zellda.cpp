#include <iostream>
#include <map>

#include <queue>

using namespace std;
int N;
int cave[125][125];
int dist[125][125];
int mov[4][2]={{1,0},{0,1},{-1,0},{0,-1}};
typedef struct xyc{
    int x,y,c;
}xyc;
bool operator<(xyc a,xyc b){
    return a.c>b.c;
}

void di(){
    priority_queue<xyc> Q;
    Q.push({0,0,cave[0][0]});
    while(!Q.empty()){
        int x=Q.top().x;
        int y=Q.top().y;
        int c=Q.top().c;
        Q.pop();
        if(x==N-1&&y==N-1) return;
        for(auto i:mov){
            if(0<=x+i[0] &&x+i[0]<N && 0<=y+i[1] &&y+i[1]<N){
                int total = cave[x+i[0]][y+i[1]]+c;
                if(total<dist[x+i[0]][y+i[1]]){
                    dist[x+i[0]][y+i[1]]=total;
                    Q.push({x+i[0],y+i[1],total});
                }
            }
        }
        
        
    }
}

int main(){
    int cnt=1;
    int temp=0;
    while(true){
        cin>>N;
        if(N==0)break;
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                
                cin>>cave[i][j];
                
                dist[i][j]=99999;
            }
        }
        di();
        cout<<"Problem "<<cnt++<<": "<<dist[N-1][N-1]<<'\n';
    }
}