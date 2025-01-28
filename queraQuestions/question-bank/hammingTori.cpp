// https://quera.org/problemset/261556
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

bool tavan2(int x) {
    return x && (!(x & (x - 1)));
}

int main() {
    int t; 
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        string bit;
        cin >> bit;

        vector<int> arr;
        int r = 0;

        while ((1 << r) < n + 1) {
            arr.push_back((1 << r) - 1);
            r++;
        }

        int error = 0;

        for (int i = 0; i < r; ++i) {
            int bitPos = (1 << i) - 1;
            int sum = 0;

            for (int j = 0; j < n; ++j) {
                if ((j + 1) & (1 << i)) { 
                    sum ^= (bit[j] - '0');
                }
            }

            if (sum != 0) {
                error += (1 << i);
            }
        }

        if (error == 0) {
            cout << "NO\n";
        } else if (error > n) {
            cout << "INVALID\n";
        } else {
            cout << "YES\n";
            bit[error - 1] = (bit[error - 1] == '0') ? '1' : '0';
            cout << bit << "\n";
        }
    }

    return 0;
}