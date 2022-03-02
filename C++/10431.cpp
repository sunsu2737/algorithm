#include <iostream>
#include <vector>
using namespace std;



int main(){
    int t;
    cin>>t;
    for (int i=0;i<t;i++){
        int answer=0;
        vector<int> v;
        int n;
        cin>>n;
        for (int j=0;j<20;j++){
            int temp;
            cin>>temp;
            v.push_back(temp);
        }
        for (int j=0;j<19;j++){
            for (int k=j+1;k<20;k++){
                if (v[j]>v[k]){
                    answer++;
                }                
            }
        }
        cout<<n<<' '<<answer<<'\n';
    }
}