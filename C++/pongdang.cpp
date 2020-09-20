#include<iostream>
using namespace std;

int N,M;

int main(){
    cin>>N>>M;
    int cnt=0;
    int flag=0;
    for(int i=0;i<M;i++){
        if(flag==0){
            cnt++;
            if(cnt==N*2) flag=1;
        }
        else if(flag==1){
            cnt--;
            if(cnt==1) flag=0;
        }

        
    }
    cout<<cnt;
}