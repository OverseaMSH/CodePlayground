https://quera.org/college/3016/chapter/8240/lesson/29201/?comments_page=1&comments_filter=ALL
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll countPairs(vector<ll>& prefix, int l, int r, ll K) {
    if (r - l <= 1) return 0;

    int m = (l + r) / 2;
    ll count = countPairs(prefix, l, m, K) + countPairs(prefix, m, r, K);

    vector<ll> left(prefix.begin() + l, prefix.begin() + m);
    vector<ll> right(prefix.begin() + m, prefix.begin() + r);
    sort(right.begin(), right.end());

    for (ll x : left) {
        ll low = x - K;
        ll high = x + K;
        count += lower_bound(right.begin(), right.end(), low) - right.begin();
        count += right.end() - upper_bound(right.begin(), right.end(), high);
    }

    inplace_merge(prefix.begin() + l, prefix.begin() + m, prefix.begin() + r);
    return count;
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        int n;
        ll K;
        cin >> n >> K;

        vector<ll> A(n);
        for (int i = 0; i < n; i++) {
            cin >> A[i];
        }

        vector<ll> prefix(n + 1);
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + A[i];
        }

        ll result = countPairs(prefix, 0, n + 1, K);
        cout <<result << endl;
    }

    return 0;
}

