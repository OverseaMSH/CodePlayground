// https://quera.org/college/4499/chapter/12640/lesson/42909/
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

bool isSharifi(int num) {
    int sum = 0, original = num, digits = 0;

    while (num > 0) {
        digits++;
        num /= 10;
    }

    num = original;

    while (num > 0) {
        int digit = num % 10;
        sum += pow(digit, digits);
        num /= 10;
    }

    return sum == original;
}

int main() {
    int n;
    cin >> n;

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int endInterval = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j) {
                endInterval += a[i] * a[j];
            }
        }
    }

    for (int i = 100; i <= endInterval; i++) {
        if (isSharifi(i)) {
            cout << i << endl;
        }
    }

    return 0;
}
