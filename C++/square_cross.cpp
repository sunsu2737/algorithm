#include<stdio.h>
#include<stdlib.h>


int main(){
    int xy10,xy11;
    int xy20,xy21;
    int XY10,XY11;
    int XY20,XY21;                   // 점들의 좌표를 순서대로 저장할 변수들

                                    //입력을 받음
    scanf("%d",&xy10);
    scanf("%d",&xy11);

    scanf("%d",&xy20);
    scanf("%d",&xy21);

    scanf("%d",&XY10);
    scanf("%d",&XY11);

    scanf("%d",&XY20);
    scanf("%d",&XY21);

    int x1,x2,y1,y2,X1,X2,Y1,Y2;            
    x1= xy10<xy20 ? xy10:xy20;      //첫번째 사각형의 두개의 x좌표중 작은것 
    x2= xy10>xy20 ? xy10:xy20;      //큰것

    y1= xy11<xy21 ? xy11:xy21;      //y좌표
    y2= xy11>xy21 ? xy11:xy21;

    X1= XY10<XY20 ? XY10:XY20;      //두번째 사각형
    X2= XY10>XY20 ? XY10:XY20;

    Y1= XY11<XY21 ? XY11:XY21;
    Y2= XY11>XY21 ? XY11:XY21;

    int dx1=X1>x1 ? X1:x1;              //두사각형의 x좌표중 작은것들중 큰것
    int dx2=X2<x2 ? X2:x2;              //두사각형의 x좌표중 큰것들중 작은것
    int dy1=Y1>y1 ? Y1:y1;                //y좌표
    int dy2=Y2<y2 ? Y2:y2;
    printf("%d",(dx2-dx1)*(dy2-dy1));       //x와y의 길이를구해서 곱

}