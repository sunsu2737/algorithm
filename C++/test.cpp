#include <stdio.h>
int x[1000000];
int main(void)
{
   int  tmp, i, j, N;

   scanf("%d", &N);

   for (i = 0; i < N; i++)
   {
      scanf("%d", &x[i]);
   }
   for (i = 0; i < 2; i++)
   {
      for (j = 0; j < N-1; j++)
      {
         if (x[j] < x[j + 1])
         {
            tmp = x[j];

            x[j] = x[j + 1];

            x[j + 1] = tmp;
         }
      }
   }
   printf("%d\n", x[N - 2]);

   return 0;
}
