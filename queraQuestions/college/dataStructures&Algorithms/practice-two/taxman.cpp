// https://quera.org/college/3016/chapter/8241/lesson/29737/?comments_page=1&comments_filter=ALL&submissions_page=1
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

bool isForbidden(string s) {
    return s == "110" || s == "101" || s == "111" || s == "011";
}

int main() {
    int n;
    cin >> n;

    if (n == 0) {
        cout << 1 << endl;
        return 0;
    }
    if (n == 1) {
        cout << 2 << endl;
        return 0;
    }
    if (n == 2) {
        cout << 4 << endl;
        return 0;
    }

    vector<vector<long long>> dp(n + 1, vector<long long>(4, 0));
    dp[2][0] = 1; // "00"
    dp[2][1] = 1; // "01"
    dp[2][2] = 1; // "10"
    dp[2][3] = 1; // "11"

    for (int i = 3; i <= n; i++) {
        for (int last2 = 0; last2 < 4; last2++) {
            string s = "";
            if (last2 == 0) s = "00";
            if (last2 == 1) s = "01";
            if (last2 == 2) s = "10";
            if (last2 == 3) s = "11";

            for (int bit = 0; bit <= 1; bit++) {
                string next3 = s + char('0' + bit);
                if (isForbidden(next3)) continue;

                int new_last2 = ((last2 << 1) & 2) | bit;
                dp[i][new_last2] = (dp[i][new_last2] + dp[i - 1][last2]) % MOD;
            }
        }
    }

    long long ans = 0;
    for (int i = 0; i < 4; i++)
        ans = (ans + dp[n][i]) % MOD;

    cout << ans << endl;
    return 0;
}
