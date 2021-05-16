#include<iostream>

using namespace std;
int N;
int game[1000][2];
int arr[1000];
int main(){
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>game[i][0]>>game[i][1];
        arr[i]=(game[i][0]-1)/(game[i][1]+1);
        
    }
    int min=99999999;
    int idx=0;
    for(int i=0;i<N;i++){
        if(min>arr[i]){
            idx=i;
            min=arr[i];
        }
    }
    cout<<idx+1<<' '<<(arr[idx]+1)*2;
}