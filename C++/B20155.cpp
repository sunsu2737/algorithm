#include <iostream>
#include <vector>
#include <cmath>
#include <map>
using namespace std;


int main(){
    int n,m;
    cin>>n>>m;
    map<int,int> ma;
    for (int i=0;i<n;i++){
        int temp;
        cin>>temp;
        if(ma.find(temp)==ma.end()){
            ma[temp]=1;
        }
        else{
            ma[temp]+=1;
        }
    }
    int answer=0;
    for(auto& i : ma){
        if (answer<i.second){
            answer=i.second;
        }
    }
    cout<<answer;

}