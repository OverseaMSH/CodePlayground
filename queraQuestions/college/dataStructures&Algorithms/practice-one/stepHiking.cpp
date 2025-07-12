// https://quera.org/college/3016/chapter/8237/lesson/29744/
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> dp(n + 1, 0);
    dp[0] = 1;

    for (int i = 1; i <= n; ++i) {
        if (i - 1 >= 0) dp[i] += dp[i - 1];
        if (i - 2 >= 0) dp[i] += dp[i - 2];
        if (i - 5 >= 0) dp[i] += dp[i - 5];
    }

    cout << dp[n] << endl;

    return 0;
}
