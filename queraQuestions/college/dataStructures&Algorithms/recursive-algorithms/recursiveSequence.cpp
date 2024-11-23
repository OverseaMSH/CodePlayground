#include <iostream>
using namespace std;
long long f(long long n)
{
    if (n == 0)
    {
        return 5;
    }
    long long temp = f(n - 1);
    if (n % 2 == 0)
    {
        return temp - 21;
    }
    else
    {
        return temp * temp;
    }
}
int main()
{
    long long n;
    cin >> n;
    cout << f(n);
}