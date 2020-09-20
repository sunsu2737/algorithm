#include<iostream>
using namespace std;
int N;

typedef struct{
    string name;
    int count;
}NC;
int main(){
    cin>>N;
    for(int i=0;i<N;i++){
        NC nc[30];
        int nc_cnt=0;
        int n;
        cin>>n;
        
        for(int j=0;j<n;j++){
            string temp;
            cin>>temp>>temp;
            if(nc_cnt==0){
                nc[nc_cnt].name=temp;
                nc[nc_cnt++].count=1;
            }
            else{
                for(int k=0;k<nc_cnt;k++){
                    if(nc[k].name.compare(temp)==0){
                        nc[k].count++;
                        break;
                    }
                    if(k==nc_cnt-1){
                        nc[nc_cnt].name=temp;
                        nc[nc_cnt++].count=1;
                        break;
                    }
                }
            }
        }
        int sum=1;
        for(int j=0;j<nc_cnt;j++){
            sum=sum*(nc[j].count+1);
        }
        cout<<sum-1<<'\n';
    }
}