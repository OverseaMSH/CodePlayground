// https://quera.org/problemset/157645
#include <iostream>
#include <string>

using namespace std;
int main()
{
    int p, l, y;
    cin >> p >> l;
    cin >> y;
    for (int i = 0; i < y; i++)
    {
        p = ((p * 2) - l);
    }
    cout << p;
    return 0;
}