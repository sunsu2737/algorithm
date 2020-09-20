#include<stdio.h>
#pragma warning(disable:4996)

int main(){
    int N;
    scanf("%d",&N); 
    int cnt=0;          //0의 갯수를 카운트
 

    while(1){
        if(10>N)break;      //N이 10보다 작을때까지 (왜냐면 10보다작을때는 0이없으니까)
        int n=N;            //n에 N을 옮겨놓고
        while(1){
            if(n<10)break;
            else{
                if(n%10==0)cnt++;       //n을 10으로나누었을때 나머지가 0이면 끝자리가 0이다
                n=n/10;                 //n을 10으로나눈다 (끝자리를 없앰) ex)1234->123
            }
        }
        N--;                
    }
    printf("%d",cnt);
}