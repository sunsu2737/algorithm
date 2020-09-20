#include<iostream>
#include<time.h>
#include<random>
#include<algorithm>
using namespace std;
random_device rd;
mt19937_64 rng(rd());
uniform_int_distribution<long long> dist(1,100000);

int randata[100000];
int revdata[100000];
clock_t s,e;
void init(){
    for (int i=0;i<100000;i++){
        randata[i]=dist(rng);
    }
    for (int i=0;i<100000;i++){
        revdata[i]=100000-i;
    }
}

void swap(int data[],int a,int b){
    int temp=data[a];
    data[a]=data[b];
    data[b]=temp;
}

void bubble(int data[],int start,int end){
    for(int i=end;i>=0;i--){
        for(int j=0;j<i;j++){
            if(data[j]>data[j+1]){
                swap(data,j,j+1);
            }
        }
    }
}
void selection(int data[],int start,int end){
    for(int i=end;i>0;i--){
        int max=0;
        int idx;
        for(int j=i;j>=0;j--){
            if(max<data[j]){
                max=data[j];
                idx=j;
            }
        }
        swap(data,i,idx);
    }
}
void insertion(int data[],int start,int end){
    for(int i=1;i<=end;i++){
        int temp=data[i];
        for(int j=i-1;j>=0;j--){
            if(temp>=data[j]){
                data[j+1]=temp;
                break;
            }
            data[j+1]=data[j];
            if(j==0){
                data[0]=temp;
                break;
            }
        }
    }
}
void mergesort(int data[],int start,int mid,int end){
    int temp[100000];
    int ts=start;
    int ds=start;
    int dm=mid+1;
    int e=end;
    while(true){
        if(data[ds]<=data[dm]){
            temp[ts++]=data[ds++];
        }
        else{
            temp[ts++]=data[dm++];
        }
        if(ds>mid || dm>end){
            break;
        }
    }
    if(ds>mid){
        while(dm<=end){
            temp[ts++]=data[dm++];
        }
    }
    else{
        while(ds<=mid){
            temp[ts++]=data[ds++];
        }
    }
    for(int i=start;i<=end;i++){
        data[i]=temp[i];
    }
}
void merge(int data[],int start,int end){
    if(start<end){
        int mid=(start+end)/2;
        merge(data,start,mid);
        merge(data,mid+1,end);
        mergesort(data,start,mid,end);
    }
}
void quick1(int data[],int start,int end){
    int pibot=end;
    int i=end;
    int j=end-1;
    if (start>=end)return;
    for(;j>=start ;j--){
        if(data[pibot]<data[j]){
            i--;
            swap(data,i,j);
        }
    }
    swap(data,i,pibot);

    quick1(data,start,i-1);
    
    quick1(data,i+1,end);
    

}
void quick2(int data[],int start,int end){
    
    int a=start;
    int b=end;
    int c=(start+end)/2;
    if(data[a]<data[b] && data[b]<data[c]){
        
    }
    else if(data[b]<data[a] && data[a]<data[c]){
        swap(data,a,b);
    }
    else{
        swap(data,c,b);
    }
    int pibot=end;
    int i=end;
    int j=end-1;
    if (start>=end)return;
    for(;j>=start ;j--){
        if(data[pibot]<data[j]){
            i--;
            swap(data,i,j);
        }
    }
    swap(data,i,pibot);

    quick2(data,start,i-1);
    
    quick2(data,i+1,end);
    
    

}
void quick3(int data[],int start,int end){
    
    
    if (start>=end)return;
    int a=rand()%(end-start+1)+start;
    int b=end;
    
    swap(data,b,a);
    
    int pibot=end;
    int i=end;
    int j=end-1;
    
    for(;j>=start ;j--){
        if(data[pibot]<data[j]){
            i--;
            swap(data,i,j);
        }
    }
    swap(data,i,pibot);

    quick3(data,start,i-1);
    
    quick3(data,i+1,end);
    
    

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
    cout.setf(ios::fixed);
    cout.precision(3);
    cout<<"----------------------------------------------------------------------------------------------------------\n";
    cout<<"               Random1000    Reverse1000    Random1000    Reverse10000    Random100000    Reverse100000\n";
    cout<<"----------------------------------------------------------------------------------------------------------\n";
    cout<<"   Bubble           ";
    init();
    s=clock();
    bubble(randata,0,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    bubble(revdata,0,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    init();
    s=clock();
    bubble(randata,0,9999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    bubble(revdata,0,9999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    init();
    s=clock();
    bubble(randata,0,99999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    bubble(revdata,0,99999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"\n";

    cout<<"   selection        ";
    init();
    s=clock();
    selection(randata,0,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    selection(revdata,0,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    init();
    s=clock();
    selection(randata,0,9999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    selection(revdata,0,9999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    init();
    s=clock();
    selection(randata,0,99999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    selection(revdata,0,99999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"\n";
    
    cout<<"   insertion        ";
    init();
    s=clock();
    insertion(randata,0,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    insertion(revdata,0,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    init();
    s=clock();
    insertion(randata,0,9999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    insertion(revdata,0,9999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"           ";
    init();
    s=clock();
    insertion(randata,0,99999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    insertion(revdata,0,99999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"\n";

    cout<<"   merge            ";
    init();
    s=clock();
    merge(randata,0,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    merge(revdata,0,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    init();
    s=clock();
    merge(randata,0,9999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    merge(revdata,0,9999);
    e=clock(); 
    cout<<float(e-s)/CLOCKS_PER_SEC<<"           ";
    init();
    s=clock();
    merge(randata,0,99999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"           ";
    s=clock();
    merge(revdata,0,99999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"\n";

    cout<<"   quick1           ";
    init();
    s=clock();
    quick1(randata,0,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    quick1(revdata,0,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    init();
    s=clock();
    quick1(randata,0,9999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    quick1(revdata,0,9999);
    e=clock(); 
    cout<<float(e-s)/CLOCKS_PER_SEC<<"           ";
    init();
    s=clock();
    quick1(randata,0,99999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"           ";
    
    cout<<"overflow"<<"\n";

    cout<<"   quick2           ";
    init();
    s=clock();
    quick2(randata,0,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    quick2(revdata,0,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    init();
    s=clock();
    quick2(randata,0,9999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    quick2(revdata,0,9999);
    e=clock(); 
    cout<<float(e-s)/CLOCKS_PER_SEC<<"           ";
    init();
    s=clock();
    quick2(randata,0,99999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"           ";
    s=clock();
    quick2(revdata,0,99999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"\n";

    cout<<"   quick3           ";
    init();
    s=clock();
    quick3(randata,0,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    quick3(revdata,0,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    init();
    s=clock();
    quick3(randata,0,9999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    quick3(revdata,0,9999);
    e=clock(); 
    cout<<float(e-s)/CLOCKS_PER_SEC<<"           ";
    init();
    s=clock();
    quick3(randata,0,99999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"           ";
    s=clock();
    quick3(revdata,0,99999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"\n";

    cout<<"   heap             ";
    init();
    s=clock();
    heapify(randata,999,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    heapify(revdata,999,999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    init();
    s=clock();
    heapify(randata,9999,9999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    heapify(revdata,9999,9999);
    e=clock(); 
    cout<<float(e-s)/CLOCKS_PER_SEC<<"           ";
    init();
    s=clock();
    heapify(randata,99999,99999);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    heapify(revdata,99999,99999);
    e=clock(); 
    cout<<float(e-s)/CLOCKS_PER_SEC<<"\n";

    cout<<"   library          ";
    init();
    s=clock();
    sort(randata,randata+1000);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    sort(revdata,revdata+1000);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    init();
    s=clock();
    sort(randata,randata+10000);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"          ";
    s=clock();
    sort(revdata,revdata+10000);
    e=clock(); 
    cout<<float(e-s)/CLOCKS_PER_SEC<<"           ";
    init();
    s=clock();
    sort(randata,randata+100000);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"           ";
    s=clock();
    sort(revdata,revdata+100000);
    e=clock();
    cout<<float(e-s)/CLOCKS_PER_SEC<<"\n";
}