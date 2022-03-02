/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

#include <iostream>
#include <vector>
#include <string>
using namespace std;


int main()
{
	int T, test_case;
	/*
	   The freopen function below opens input.txt file in read only mode, and afterward,
	   the program will read from input.txt file instead of standard(keyboard) input.
	   To test your program, you may save input data in input.txt file,
	   and use freopen function to read from the file when using cin function.
	   You may remove the comment symbols(//) in the below statement and use it.
	   Use #include<cstdio> or #include <stdio.h> to use the function in your program.
	   But before submission, you must remove the freopen function or rewrite comment symbols(//).
	 */	

	// freopen("input.txt", "r", stdin);

	cin >> T;
	for(test_case = 0; test_case  < T; test_case++)
	{

        int n,t;
        cin>>n>>t;
        vector<int> arr(n);
        // cout<<"debug";
        string s ;
        cin>>s;
        vector<char> brr(n);
        copy(s.begin(), s.end(), brr.begin());
        
        for (int i=0;i<t;i++){
            if (i+t>=n) break;
            if (brr[i]=='1') arr[i+t]=1;
            else arr[i+t]=-1;
        }
        for (int i=n-1;i>=n-t;i--){
            if (i-t<0) break;
            if (brr[i]=='1') arr[i-t]=1;
            else arr[i-t]=-1;
        }
        for (int i=t;i<n-t;i++){
            if (brr[i]=='0'){
                arr[i+t]=-1;
                arr[i-t]=-1;
            }

                

            
        }
        for (int i=t;i<n-t;i++){
            if(brr[i]=='1'){
                if (arr[i-t]==0 and arr[i+t]==0){
                    arr[i+t]=1;
                }
                else if(arr[i-t]==-1 and arr[i+t]==0) arr[i+t]=1;
                else if(arr[i+t]==-1 and arr[i-t]==0) arr[i-t]=1;

                

            }
        }
                
		
		cout << "Case #" << test_case+1 << endl;
		for(int i=0;i<n;i++){
            if (arr[i]==-1) cout<<0;
            else    cout<<arr[i];
        }
        cout<<'\n';
	}

	return 0;//Your program should return 0 on normal termination.
}