// https://quera.org/problemset/618
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int m = (2 * n) + 1;
    for (int i = 0; i < m; i++)
    {
        if (i % 2 == 0)
        {
            continue;
        }
        else
        {
            for (int k = n; k > i / 2; k--)
            {
                cout << " ";
            }
            for (int j = 0; j < i; j++)
            {
                cout << "*";
            }
            cout << endl;
        }
    }
    for (int z = 0; z < m; z++)
    {
        cout << "*";
    }
    cout << endl;
    for (int a = 0; a < m; a++)
    {
        if (a % 2 == 0)
        {
            continue;
        }
        else
        {
            for (int b = 0; b <= a / 2; b++)
            {
                cout<<" ";
            }
            for (int c = m - 1; c > a; c--)
            {
                cout << "*";
            }
            cout << endl;
        }
    }
    return 0;
}