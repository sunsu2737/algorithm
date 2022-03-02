#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n,x,k;
    cin>>n>>x>>k;
    vector<int> v(n);
    v[x-1]=1;

    for (int i=0;i<k;i++){
        int to,from;
        cin>>to>>from;
        int temp=v[to-1];
        v[to-1]=v[from-1];
        v[from-1]=temp;
    }
    for (int i=0;i<n;i++){
        if (v[i]==1){
            cout<<i+1;
            break;
        }
    }
}