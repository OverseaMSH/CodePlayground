// https://quera.org/problemset/651
#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int main() {
    long long a, b, c;

    cin >> a >> b >> c;

    long long result = 0;
    int index = 0;
    while (a != 0) {
        int s = a % 10;
        result += s * pow(b, index);
        a /= 10;
        index++;
    }

    vector<int> digits;
    while (result != 0) {
        digits.push_back(result % c);
        result /= c;
    }

    int n = digits.size();
    for (int i = 0; i < n / 2; i++) {
        if (digits[i] != digits[n - 1 - i]) {
            cout << "NO";
            return 0;
        }
    }

    cout << "YES";
    return 0;
}
