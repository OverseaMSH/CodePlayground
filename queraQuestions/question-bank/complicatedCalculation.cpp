// https://quera.org/problemset/279
#include <iostream>
#include <string>
#include <math.h>
#include <cmath>
using namespace std;
int factoriel(int b)
{
    int c = 1;
    for (int i = 1; i <= b; i++)
    {
        c *= i;
    }
    return c;
}
int main()
{
    int x, a, n, sum;
    sum = 0;
    cin >> x >> a >> n;
    for (int k = 0; k <= n; k++)
    {
        sum += (factoriel(n) / (factoriel(k) * factoriel(n - k))) * pow(x, k) * pow(a, n - k);
    }
    cout << sum;
}