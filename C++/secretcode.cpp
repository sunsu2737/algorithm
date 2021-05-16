#include<iostream>
#include<string>
using namespace std;
string N;
int dp[5010];


void get(){
  
    for(int i=0;i<N.length();i++){
        if (i==0 && N[i]=='0'){
            
            break;
        }
        else if(i==0){
            dp[i]=1;
        }
        else if(i==1){
            if(N[i]!='0'){
                if((N[i-1]-'0')*10+(N[i]-'0')<=26){
                    dp[i]=2;
                }
                else{
                    dp[i]=1;
                }
            }
            else{
                if((N[i-1]-'0')*10+(N[i]-'0')<=26){
                    dp[i]=1;
                }
                else{
                    
                    break;
                }
            }
        }
        else{
            if(N[i]!='0'){
                if(N[i-1]=='0'){
                    dp[i]=dp[i-1];
                }
                else if((N[i-1]-'0')*10+(N[i]-'0')<=26){
                    dp[i]=(dp[i-2]+dp[i-1])%1000000;
                }
                else{
                    dp[i]=dp[i-1];
                }
            }
            else{
                if(N[i-1]=='0'){
                    break;
                }
                else if((N[i-1]-'0')*10+(N[i]-'0')<=26){
                    dp[i]=dp[i-2];
                }
                else{
                    
                    break;
                }
            }
        }
    }
}

int main(){
    cin>>N;
    get();
    cout<<dp[N.length()-1]%1000000;
    

}