#include <iostream>
using namespace std;
long long int A, B;
long long int cnt;

void goldminsu(long long int num)
{
    if (num > B)
        return;
    if (A <= num && num <= B)
        cnt++;

    goldminsu(num * 10 + 4);
    goldminsu(num * 10 + 7);
}

int main()
{
    cin >> A >> B;

    goldminsu(4);
    goldminsu(7);

    cout<<cnt;
}