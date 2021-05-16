#include<iostream>
using namespace std;
string S;

int main(){
    cin>>S;
    int sum=0;
    int answer=0;
    int flag=0;
    
    for(auto i: S){
        if('0'<=i&&i<='9'){
            sum=sum*10+i-'0';
        }
        else if (i=='+'){
            if(flag==0){
                answer+=sum;
                sum=0;
            }
            else{
                answer-=sum;
                sum=0;
            }
        }
        else if (i=='-'){
            if(flag==0){
                answer+=sum;
                sum=0;
            }
            else{
                answer-=sum;
                sum=0;
            }
            flag++;
        }
        
        
    }
    if(flag==0){
                answer+=sum;
                sum=0;
            }
            else{
                answer-=sum;
                sum=0;
            }
    cout<<answer;

}