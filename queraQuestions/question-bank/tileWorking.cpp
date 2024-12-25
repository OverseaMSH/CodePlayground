// https://quera.org/problemset/605
#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;

int countWays(int n) {
    if (n == 1) return 1;
    if (n == 2) return 2;

    vector<int> dp(n + 1);
    dp[1] = 1;
    dp[2] = 2;

    for (int i = 3; i <= n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
    }

    return dp[n];
}

int main() {
    int n;
    cin >> n;
    cout << countWays(n) << endl;
    return 0;
}
