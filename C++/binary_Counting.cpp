#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int n, k;
queue<int> B;
vector<int> A;
int main()
{
    cin >> n >> k;
    int flag = k;
    int end = k + 4 * n;
    int num = 0;
    int num2 = 1;

    for (int i = 1; i <= end*100; i++)
    {
        int answer = num % 2;
        num = num / 2;
        A.push_back(answer);
        if (num == 0 )
        {
            num = num2;
            num2++;
            while (!A.empty())
            {
                B.push(A.back());
                A.pop_back();
            }
        }
    }

    for (int i = 1; i <= end; i++)
    {
        int answer = B.front();
        B.pop();
        if (i == flag)
        {
            cout << answer << ' ';
            flag += n;
        }
    }
}