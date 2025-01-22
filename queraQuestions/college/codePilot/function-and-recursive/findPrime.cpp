// https://quera.org/college/4499/chapter/12640/lesson/42906
#include <iostream>
#include <cmath> 
using namespace std;

bool isPrime(long long n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (long long i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

int main() {
    long long n;
    cin >> n;
    long long num = n;
    long long b = 0; 

    while (num > 0) {
        b += num % 10;
        num /= 10;
    }
    while (b != 0) {
        n++;
        if (isPrime(n)) {
            b--;
        }
    }
    cout << n;
    return 0;
}
