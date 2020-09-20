#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;

int N,M;
char house[2][51][51];
int S[2],E[2];
int X[6][2];
int Xcnt=0;
vector<int> Xper;

int goout(int sx,int sy,int ex,int ey){
    queue<vector<int> > Q;
    Q.push({sx,sy,0});
    while(!Q.empty()){
        vector<int> V=Q.front();
        int c=V.back();
        V.pop_back();
        int y=V.back();
        V.pop_back();
        int x=V.back();
        V.pop_back();
        Q.pop();

        if(x==ex&&y==ey){
            return c;
        }

        if(0<=x+1 && x+1<M && 0<=y && y<N && house[1][x+1][y]!='#'){
            
                house[1][x+1][y]='#';
                Q.push({x+1,y,c+1});
            
        }
        if(0<=x && x<M && 0<=y+1 && y+1<N && house[1][x][y+1]!='#'){
            
            
                house[1][x][y+1]='#';
                Q.push({x,y+1,c+1});
            
        }
        if(0<=x-1 && x-1<M && 0<=y && y<N && house[1][x-1][y]!='#'){
            
                house[1][x-1][y]='#';
                Q.push({x-1,y,c+1});
                
        }
        if(0<=x && x<M && 0<=y-1 && y-1<N && house[1][x][y-1]!='#'){
            
                house[1][x][y-1]='#';
                Q.push({x,y-1,c+1});
            
        }
    }
    return 9999;
}


void copyhouse2(){
    for(int i=0;i<M;i++){
        for(int j=0;j<N;j++){
            
            house[1][i][j]=house[0][i][j];
            
        }
    }
}

int main(){
    cin>>N>>M;
    for(int i=0;i<M;i++){
        for(int j=0;j<N;j++){
            cin>>house[0][i][j];
            house[1][i][j]=house[0][i][j];
            if(house[0][i][j]=='X'){
                X[Xcnt][0]=i;
                X[Xcnt][1]=j;
                Xper.push_back(Xcnt);
                Xcnt++;
            }
            else if(house[0][i][j]=='S'){
                S[0]=i;
                S[1]=j;
            }
            else if(house[0][i][j]=='E'){
                E[0]=i;
                E[1]=j;
            }
        }
    }
    int min=99999999;
    do{
        int Sx=S[0],Sy=S[1];
        int cnt=0;
        
        for(int i=0;i<Xcnt;i++){
            cnt+=goout(Sx,Sy,X[Xper[i]][0],X[Xper[i]][1]);
            Sx=X[Xper[i]][0];
            Sy=X[Xper[i]][1];
            copyhouse2();

        }
        cnt+=goout(Sx,Sy,E[0],E[1]);
        copyhouse2();
        if(min>cnt){
            min=cnt;
        }
    }while(next_permutation(Xper.begin(),Xper.end()));
    cout<<min;
    
}