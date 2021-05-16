#include<iostream>
using namespace std;
int N;
int arr[501][501];
int dp[501][501];


void intTrianggle(){
    for(int i=1;i<=N;i++){
        for(int j=1;j<=i;j++){
            if(dp[i-1][j-1]>dp[i-1][j]){
                dp[i][j]=dp[i-1][j-1]+arr[i][j];
                
            }
            else{
                dp[i][j]=dp[i-1][j]+arr[i][j];
            }
        }
    }
}

int main(){
    cin>>N;
    for(int i=1;i<=N;i++){
        for(int j=1;j<=i;j++){
            cin>>arr[i][j];
        }
    }
    intTrianggle();
    int max=0;
    for(int i=1;i<=N;i++){
        if(dp[N][i]>max){
            max=dp[N][i];
        }
    }
    cout<<max;

    
}