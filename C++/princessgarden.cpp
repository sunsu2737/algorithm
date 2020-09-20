#include <iostream>
#include <algorithm>
using namespace std;

int N;
int arr[100001][2];
int Start = 60;
int End = 334;
int idx;
int cnt = 0;

bool operator>(int a[2],int b[2]){
    return 
}

void garden()
{
    
    while (1)
    {
        int maxs=0;
        int idxs=-1;
        
        if(Start>End){
            cout<<cnt;
            return;
        }
        for(int i=0; i<N;i++){
            if(arr[i][0]<=Start&&Start<arr[i][1]){
                if(maxs<arr[i][1]-Start){
                    idxs=i;
                    maxs=arr[i][1]-Start;
                }
            }
            
            
        }
        if(idxs!=-1){
            Start=arr[idxs][1];
            cnt++;
        }
        
        if(idxs==-1){
            if(Start<=End){
                cout<<0;
                return;
            }
        }
        
    }
}

int main()
{
    cin >> N;
    int max = 0;
    for (int i = 0; i < N; i++)
    {
        int ms, ds, me, de;
        cin >> ms >> ds >> me >> de;
        for (int j = 1; j < ms; j++)
        {
            if (j == 1 || j == 3 || j == 5 || j == 7 || j == 8 || j == 10 || j == 12)
            {
                arr[i][0] += 31;
            }
            else if (j == 4 || j == 6 || j == 9 || j == 11)
            {
                arr[i][0] += 30;
            }
            else
            {
                arr[i][0] += 28;
            }
        }
        arr[i][0] += ds;
        for (int j = 1; j < me; j++)
        {
            if (j == 1 || j == 3 || j == 5 || j == 7 || j == 8 || j == 10 || j == 12)
            {
                arr[i][1] += 31;
            }
            else if (j == 4 || j == 6 || j == 9 || j == 11)
            {
                arr[i][1] += 30;
            }
            else
            {
                arr[i][1] += 28;
            }
        }
        arr[i][1] += de;

       
    }
    
    garden();
}