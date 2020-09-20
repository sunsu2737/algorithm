#include <stdio.h>

int main()
{
    int year;
    scanf("%d",&year);

    if(year%4==0){
        if (year%100==0){
            if(year%400==0){
                printf("윤년입니다.");
            }
            else
                printf("윤년이아닙니다.");
        }
        else{
            printf("윤년입니다.");
        }
        
    }
    else{
        printf("윤년이아닙니다.");
    }
}

