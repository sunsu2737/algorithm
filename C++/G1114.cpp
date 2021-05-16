#include<iostream>
#include<cstring>
#include<set>
#include<algorithm>

#include<vector>
using namespace std;

int L,K,C;
int cut[10001];
set<int> check;
int flag[10001];
set<int> S;
int value=-1;
int Min=INT32_MAX;
void B_search(int data[],int start,int end,int D){
    int middle=(start+end)/2;
    if(start>=end){
        if(Min>=abs(D-data[middle])){
            if(Min==abs(D-data[middle])){
                if(data[middle]<data[value]){
                    Min=D-data[middle];
                    value=middle;
                }
            }
            else{
            Min=D-data[middle];
            value=middle;
            }
        
        }
        
        
        return;
    }
    if(data[middle]==D ) {
        value=middle;
      
        return;
    } 
    else if(data[middle]>D) {
        if(Min>data[middle]-D){
            Min=data[middle]-D;
            value=middle;
        }
        B_search(data,start,middle-1,D);
    }
    else if(data[middle]<D) {
        if(Min>=D-data[middle]){
            Min=D-data[middle];
            value=middle;
        }
        B_search(data,middle+1,end,D);
    }
}

int main(){
    cin>>L>>K>>C;
    
    for(int i=0;i<K;i++){
        cin>>cut[i];
    }
    sort(cut,cut+K);
    int temp=L/(C+1);
    for(int i=0;i<C;i++){
        flag[i]=temp;
        temp=temp+L/(C+1);
    }
    int arr[10001];
    int ans;
    for(int i=0;i<C;i++){
        B_search(cut,value+1,K-1,flag[i]);
        arr[i]=cut[value];
        Min=INT32_MAX;
        if(i==0){
            ans=cut[value];
        }
    }
    sort(arr,arr+C);
    int max=0;
    for(int i=0;i<C;i++){
        if(i==0){
            max=arr[i];
        }
        else if(max<arr[i]-arr[i-1]){
            max=arr[i]-arr[i-1];
        }
    }
    if(max<L-arr[C-1]){
        max=L-arr[C-1];
    }
    cout<<max<<' '<<ans;
    


}
