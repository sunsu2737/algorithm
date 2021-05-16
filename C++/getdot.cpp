#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int x[100000];
int y[100000];
int sum=0;
int main()
{
    cin >> N >> M;
    
    for (int i = 0; i < M; i++)
    {
        cin >> x[i] >> y[i];
        
    }
    sort(x, x + M);
    sort(y, y + M);
    int middle_x = x[M / 2] ;
    int middle_y = y[M / 2] ;
    for(int i=0;i<M;i++){
        if(x[i]-middle_x<0){
            sum+=-(x[i]-middle_x);
        }
        else{
            sum+=x[i]-middle_x;
        }
        if(y[i]-middle_y<0){
            sum+=-(y[i]-middle_y);
        }
        else{
            sum+=y[i]-middle_y;
        }
    }
    cout<<sum;
}