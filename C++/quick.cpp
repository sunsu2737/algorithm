#include<iostream>
#include<time.h>
#include<algorithm>
#include<random>
#include<stdlib.h>
using namespace std;
random_device rd;
mt19937_64 rng(rd());
uniform_int_distribution<__int64> dist(1,100000);

void swap(int data[],int a,int b){
    int temp=data[a];
    data[a]=data[b];
    data[b]=temp;
}


void heapify(int data[],int end,int size){
    int i=end;
    if (i<0) return;
    if (i*2>size) heapify(data,end-1,size);
    else{
        while(i*2<=size){
        
            if(i*2+1<=size){
                if(data[i*2]<data[i*2+1]){
                    if(data[i]<data[i*2+1]){
                        swap(data,i,i*2+1);
                        i=i*2+1;
                    }
                    else break;

                }
                else{
                    if(data[i]<data[i*2]){
                        swap(data,i,i*2);
                        i=i*2;
                    }
                    else break;
                }
            }
            else{
                if(data[i]<data[i*2]){
                        swap(data,i,i*2);
                        i=i*2;
                    }
                    else break;
            }
                
            
        }
        heapify(data,end-1,size);
    }
}

int main(){
    srand((unsigned int)time(NULL));
    int a[]={1,2,7,6,4,3,5};
    sort(a,a+7);
    for(auto i: a){
        cout<<i<<' ';
    }
}