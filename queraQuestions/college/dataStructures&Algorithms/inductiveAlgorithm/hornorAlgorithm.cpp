#include <iostream>
using namespace std;

int main()
{
    int n, x;
    const int MOD = 1000000007;
    cin >> n >> x;

    long long result = 0;
    long long coef;

    for (int i = 0; i <= n; i++)
    {
        cin >> coef;
        result = (result * x + coef) % MOD;
    }

    cout << result << endl;
    return 0;
}
