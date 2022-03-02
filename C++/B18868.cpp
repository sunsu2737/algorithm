#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
using namespace std;

// int fac(int n){
//     int result=1;
//     for (int i=1;i<n+1;i++){
//         result*=i;
//     }
//     return result;
// }

// int combi(int n,int r){
//     return fac(n)/(fac(n-r)*fac(r));
// }

int main(){

    int answer=0;
    map<string,int> v;
    int m,n;
    cin>>m>>n;
    for (int i=0;i<m;i++){

        vector<int> temp;
        string temp2;
        for (int j=0;j<n;j++){
            int p;
            cin>>p;
            temp.push_back(p);

        }
        for (int j=0;j<n-1;j++){
            for (int k=j+1;k<n;k++){
                
            
                if(temp[j]<temp[k]){
                    temp2.push_back('<');
                }
                else if(temp[j]==temp[k]){
                    temp2.push_back('=');
                }
                else{
                    temp2.push_back('>');
                }
            }
        }   
        if (v.find(temp2)==v.end()){
            v[temp2]=1;     
        }    
        else{
            v[temp2]+=1;
        }

        
    }
    for(auto& i:v){
        // cout<<i.first<<" "<<i.second<<endl;
        answer+=i.second*(i.second-1)/2;
    }
    cout<<answer;
}

