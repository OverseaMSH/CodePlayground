// https://quera.org/college/3016/chapter/8238/lesson/27732/?comments_page=1&comments_filter=ALL&submissions_page=1
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> a(n + 1);
    for (int i = 0; i <= n; ++i) {
        cin >> a[i];
    }

    vector<vector<long long>> dp(n, vector<long long>(n, 0));

    for (int length = 2; length <= n; ++length) {
        for (int l = 0; l <= n - length; ++l) {
            int r = l + length - 1;
            dp[l][r] = LLONG_MAX; 
            for (int k = l; k < r; ++k) {
                long long cost = dp[l][k] + dp[k + 1][r] + 1LL * a[l] * a[k + 1] * a[r + 1];
                dp[l][r] = min(dp[l][r], cost);
            }
        }
    }

    cout << dp[0][n - 1] << endl;

    return 0;
}
