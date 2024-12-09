#include <iostream>
using namespace std;
int fib(int n) {
    if (n == 0) return 0;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

int main()
{
    int n;
    cin >> n;
    cout << fib(n);
}