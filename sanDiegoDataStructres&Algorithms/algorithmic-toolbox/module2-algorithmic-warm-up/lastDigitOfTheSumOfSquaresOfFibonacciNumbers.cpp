#include <iostream>
using namespace std;

long long fib(long long n) {
    long long a = 0, b = 1;
    for (long long i = 2; i <= n; ++i) {
        long long temp = (a + b) % 10;
        a = b;
        b = temp;
    }
    return (n == 0) ? 0 : b*b;
}

int main() {
    long long n;
    cin >> n;
    long long sum=0;
    for(long long i=0;i<n+1;i++){
        sum+=fib(i)%10;
    }
    cout << sum%10 << endl;
    return 0;
}
