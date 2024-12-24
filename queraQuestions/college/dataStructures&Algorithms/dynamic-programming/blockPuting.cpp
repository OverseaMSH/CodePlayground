
#include <iostream>
using namespace std;

const int MOD = 1000000007;
const int MAX_N = 100000;

long long f[MAX_N + 1];

void precompute() {
    f[0] = 1;
    f[1] = 1;
    f[2] = 1;
    f[3] = 2;
    
    for (int i = 4; i <= MAX_N; i++) {
        f[i] = (f[i - 1] + f[i - 2] + f[i - 3] - f[i - 4]) % MOD;
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
