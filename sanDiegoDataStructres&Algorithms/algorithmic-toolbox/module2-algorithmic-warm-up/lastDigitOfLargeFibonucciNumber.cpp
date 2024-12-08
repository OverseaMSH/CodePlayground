#include <iostream>
using namespace std;

long long fib(long long n) {
    if (n == 0) return 0;
    long long a = 0, b = 1;
    for (long long i = 2; i <= n; ++i) {
        long long temp = (a + b) % 10;
        a = b;
        b = temp;
    }
    return b;
}

int main() {
    long long n;
    cin >> n;
    cout << fib(n) % 10 << endl;
}
