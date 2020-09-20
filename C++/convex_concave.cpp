#include<stdio.h>
#pragma warning(disable:4996)

int main(){
    int pre;                //이전의수
    int next;               //현재 수
    int flag=0;             //전체 수열의 상태 0==both 1==convex 2==concave 3==None
    int flag2=0;            // 이전의수와 현재 수의 상태 감소==-1 증가 ==1
    int change=0;           // 변화 횟수 ex) 증가 ->감소 == change++; 두번이상바뀌면 None
    scanf("%d ",&pre);
    scanf("%d ",&next);
    while(1){
        if(next==-1){
            break;
        }
        if(next<pre){                   // 현재수가 이전수보다 작으면 즉감소하면
            if(flag2==0 || flag2==-1){      // 이전수 가 그전수보다 작거나 같았을때
                flag2=-1;                       //상태는 그대로
            }
            else if(flag2==1){          //이전수가 그전수보다 컷을때 즉 증가 중이었을때
                flag2=-1;               //상태를 업데이트해주고
                change++;               //변화 횟수를 증가
                
                if(change==1)           //변화 횟수가 한번이면
                flag=1;                 //볼록
                else if(change==2){     //변화횟수가 두번이상이면 None을하고 종료
                    flag=3;
                    break;
                }
            

               
            }
        }
        else if(next>pre){              //현재수가 이전수보다 크면 즉 증가
            if(flag2==0||flag2==1){     // 이전수가 그전 수보다 크거나 같았으면
                flag2=1;                // 상태는 그대로
            }
            else if(flag2==-1){         //이전수가 그전 수보다 작았으면 즉 감소
                flag2=1;                //상태 변화
                change++;               //변화횟수 증가
                if(change==1)           //변화횟수가 한번이면
                flag=2;                 //오목
                else if(change==2){     //변화횟수가 두번이상이면 None을하고 종료
                    flag=3;
                    break;
                }
            }
        }
        pre=next;
        scanf("%d ",&next);
        
    }
    if(flag==0){
        printf("Both");
    }
    else if(flag==1){
        printf("Convex");
    }
    else if(flag==2){
        printf("Concave");
    }
    else if(flag==3){
        printf("None");
    }
}