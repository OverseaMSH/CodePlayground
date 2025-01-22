https://quera.org/college/3016/chapter/8238/lesson/27723/
#include <iostream>
using namespace std;

const int MOD = 1e9 + 7;
const int MAX_N = 1e5;

long long f[MAX_N + 1];

void precompute() {
    f[0] = 1;
    f[1] = 1;
    f[2] = 1;
    f[3] = 2;
    for (int i = 4; i <= MAX_N; i++) {
        f[i] = (f[i - 1] + f[i - 2] + f[i - 3]) % MOD;
        if (i - 4 >= 0) {
            f[i] = (f[i] - f[i - 4] + MOD) % MOD;
        }
    }
}

int main() {
    int q;
    cin >> q;
    precompute();
    while (q--) {
        int n;
        cin >> n;
        cout << f[n] << endl;
    }
    return 0;
}