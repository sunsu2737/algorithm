#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std;

map<char,char> m={{'I','E'},{'E','I'},{'S','N'},{'N','S'},{'T','F'},{'F','T'},{'J','P'},{'P','J'}};
int main(){
    string s;
    cin>>s;
    for (auto i :s){
        cout<<m[i];
    }
}