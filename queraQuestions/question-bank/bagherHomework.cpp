// https://quera.org/problemset/10230
#include <iostream>
#include <string>

using namespace std;
int main()
{
    int a1, a2, a3;
    cin >> a1 >> a2 >> a3;
    if (a1==0 || a2==0 || a3==0 || a1+a2+a3!=180){
        cout << "NO";
    }else{
        cout << "YES";
    }
    return 0;
}
