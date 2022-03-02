#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n;
    int answer=0;
    cin>>n;
    vector<int> v;
    for (int i=0;i<n;i++){
        int temp;
        cin>>temp;
        v.push_back(temp);
    }
    while(v.size()>1){
        int max_idx=max_element(v.begin(), v.end()) - v.begin();
        if(max_idx==0){
            answer+=v[max_idx]+v[max_idx+1];
            v[max_idx+1]=v[max_idx];
            v.erase(v.begin()+max_idx);
        }
        else if(max_idx==v.size()-1){
            answer+=v[max_idx]+v[max_idx-1];
            v[max_idx-1]=v[max_idx];
            v.erase(v.begin()+max_idx);
        }
        else{
            if (v[max_idx-1]>v[max_idx+1]){
                answer+=v[max_idx]+v[max_idx+1];
                v[max_idx+1]=v[max_idx];
                v.erase(v.begin()+max_idx);
            }
            else{
                answer+=v[max_idx]+v[max_idx-1];
                v[max_idx-1]=v[max_idx];
                v.erase(v.begin()+max_idx);
            }
        }
    }
    cout<<answer;
}