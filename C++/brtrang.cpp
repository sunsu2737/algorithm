#include<iostream>
using namespace std;
int n;
int prime[246914];

void get_prime(){
    prime[0]=1;
    prime[1]=1;
    for(int i=2;i<=246913;i++){
        if(prime[i]==0){
            for(int j=i+i;j<=246913;j=j+i){
                prime[j]=1;
            }
        }
    }
    
}


int counting(){
    int cnt=0;
    for(int i=n+1;i<=n*2;i++){
        if(prime[i]==0){
            cnt++;
        }
    }
    return cnt++;
}

int main(){
    get_prime();
    while(1){
        cin>>n;
        if(n==0) break;
        cout<<counting()<<'\n';
    }
}