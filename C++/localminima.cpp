#include<stdio.h>
#pragma warning(disable:4996)
int main(){
    int cnt=0;          //로컬미니마의 갯수
    int pre=200000000;  //첫번째수일때는 뒤의수만보면되므로
    int middle=-1;          //현재수
    int next=-1;            //다음수
    scanf("%d ",&middle);   //첫수와
    scanf("%d ",&next);     //다음수를 입력
    while(1){
        if(middle<=pre && middle<=next){        //현재수가 이전수와 다음수보다 작으면
            cnt++;                  //갯수 1증가
        }
        pre=middle;         //현재수를 이전수로 옮기고
        middle=next;        //현재수에 다음수를 넣고
        scanf("%d ",&next); //다음수를 입력 받는다
        if(next==-1){       //다음수가 -1 이면 종료
            if(middle<=pre){
                cnt++;
            }
            break;
        }
        
    }
    printf("%d",cnt);

}