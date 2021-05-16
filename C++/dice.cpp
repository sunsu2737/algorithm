#include<stdio.h>
#include<stdlib.h>    //랜덤함수를사용하기위한 헤더
#include<time.h>        //시간에대한 헤더
#pragma warning(disable:4996)

int main(){
    srand((unsigned int)time(NULL));    //랜덤함수의 시드를 시간으로 설정
    int first=0;                        //6번굴릴때 1이 1번이상 나온횟수를 카운트
    int secend=0;                       // 두번째상황 카운트
    for(int i=0;i<1000000;i++){
        int dice2=0;                    //두번째상황에서 1이나온횟수
        for(int j=0;j<6;j++){
            if(1==rand()%6+1){          //주사위를굴려서 1이나오면 횟수증가후 종료
                first++;
                break;
            }      
        }
        for(int j=0;j<12;j++){
            if(1==rand()%6+1){          //주사위를굴려서 1이나오면 횟수증가후
                dice2++;
                if(dice2>1){                //횟수가 2회가되면 카운트하고 종료
                    secend++;
                    break;
                }
            }        
        }
        
    }
    printf("6번굴려서 적어도 1번 1이 나올 확률: %f\n",(double(first)/1000000));
    printf("6번굴려서 적어도 2번 1이 나올 확률: %f",(double(secend)/1000000));
}