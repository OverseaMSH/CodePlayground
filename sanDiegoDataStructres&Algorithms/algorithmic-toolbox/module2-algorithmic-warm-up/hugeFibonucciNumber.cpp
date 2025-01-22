#include <iostream>
using namespace std;

long long fib(long long n, long long m) {
    long long a = 0, b = 1;
    for (long long i = 2; i <= n; ++i) {
        long long temp = (a + b) % m;
        a = b;
        b = temp;
    }
    return (n == 0) ? 0 : b;
}

int main() {
    long long n, m;
    cin >> n >> m;
    cout << fib(n, m) << endl;
    return 0;
}
