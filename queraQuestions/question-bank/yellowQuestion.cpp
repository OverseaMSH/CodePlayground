// https://quera.org/problemset/3537
#include <iostream>
#include <string>

using namespace std;
int main()
{
    int n;
    string o="";
    cin >> n;
    for(int start=1; start <= n ; start++){
        o+="o";
    }
    cout << "W"+o+"w!";
    return 0;
}