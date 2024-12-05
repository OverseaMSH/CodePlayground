// https://quera.org/problemset/589
#include <iostream>
#include <string>

using namespace std;
int main()
{
    int n, m = 1;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        m *= i;
    }
    cout << m;

    return 0;
}