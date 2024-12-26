#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;
const int MAX_N = 2000;

vector<vector<long long>> comb(MAX_N + 1, vector<long long>(MAX_N + 1, 0));

void calculateCombinations() {
    for (int i = 0; i <= MAX_N; ++i) {
        for (int j = 0; j <= i; ++j) {
            if (j == 0 || j == i) {
                comb[i][j] = 1;
            } else {
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD;
            }
        }
    }
}

int main() {
    calculateCombinations();
    
    int q;
    cin >> q;
    while (q--) {
        int n, r;
        cin >> n >> r;
        if (r > n) {
            cout << 0 << endl;
        } else {
            cout << comb[n][r] << endl;
        }
    }
    
    return 0;
}