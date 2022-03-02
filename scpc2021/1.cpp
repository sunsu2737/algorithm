#include <iostream>
#include <vector>
using namespace std;

int main(){
    int t,n;
    cin>>t;
    for(int i=0; i<t; i++){
        vector<int> arr;
        int answer=0;
        cin>>n;
        vector<int> check(n);
        for (int j=0;j<n;j++){
            int temp;
            cin>>temp;
            arr.push_back(temp);
        }
        
        for (int j=0;j<n;j++){
            if (check[j]==0){
                answer+=1;
                int x=j;
                while (true){
                    // cout<<j<<x<<endl;
                    if (check[x]==1){
                        answer-=1;
                        break;
                    }
                    check[x]=1;
                    x=x+arr[x];
                    if (x>=n){
                        break;
                    }    
                }
            }
        }
        cout << "Case #" << i+1 << endl;
		cout << answer << endl;
    }
}