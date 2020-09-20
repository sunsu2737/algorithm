#include <stdio.h>

int main()
{
   int a[][3]={{1,2,3},{4,5,6}};

   printf("%d",a);
   // printf("sizeof int=%d\n", sizeof(int));
   // printf("sizeof float=%d\n", sizeof(float));
   // printf("sizeof double=%d\n", sizeof(double));
   // printf("sizeof char=%d\n", sizeof(char));
   // printf("sizeof long=%d\n", sizeof(long));
   // printf("sizeof long long int=%d\n", sizeof(long long int));

   // printf("%d\n", __INT32_MAX__);
   // printf("%d\n", __INT32_MAX__ + 1);

   // char a = 'a';
   // char z = 'z';
   // char A = 'A';
   // char Z = 'Z';
   // printf("a=%d\n", a+1);
   // printf("z=%d\n", z);
   // printf("A=%d\n", A);
   // printf("Z=%d\n", Z);

   // char my_char;
   // printf("시저암호: 각 문자를 다른문자로 치환시켜 다른문자열로 암호화시키는것 version1\n");
   // printf("입력: ");
   // scanf("%c", &my_char);
   // my_char +=3 ;
   // if (my_char>122){
   //    my_char-=26;
   // }
   // printf("+3하여 바뀐문자: %c\n",my_char);

   // int i=0;
   // loop:
   // if (i<5){

   //    printf("%d\n",i);
   //    printf("실행");

   //    i++;
   //    goto loop;
   // }

   // int a, b, c;

   // for (a = 1; a <= 100; a++)
   //    for (b = 1; b <= 100; b++)
   //       for (c = 1; c <= 100; c++)
   //          if ((a * a + b * b) == c * c)
   //             printf("%d %d %d\n", a, b, c);

   // int flag = 0;
   // for (int i = 1; i <= 50; i++)
   // {
   //    if (i % 2 == 0)
   //    {
   //       printf("%-5d", i);
   //       flag++;
   //    }
   //    if (flag % 10 == 0)
   //    {
   //       printf("\n");
   //    }
   // }
}