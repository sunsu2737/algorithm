#include <iostream>
#include <string>

using namespace std;

int N;
string A[100];
string S;
int dp[101];

void string_judge()
{
dp[S.size()] = 1;
for (int i = S.size() - 1; i >= 0; i--)
{
    for (int j = 0; j < N; j++)
    {
        if (S.find(A[j], i) == i && dp[i + A[j].size()] == 1)

            dp[i] = 1;
            
        
    }
}
}

int main()
{
cin >> S;
cin >> N;

for (int i = 0; i < N; i++)
{
    cin >> A[i];
}
string_judge();
cout<<dp[0];
}
