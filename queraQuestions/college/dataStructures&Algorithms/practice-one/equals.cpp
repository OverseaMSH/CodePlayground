// https://quera.org/college/3016/chapter/8237/lesson/29950/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int &x : a) cin >> x;

    if (n >= 20) {
        cout << "YAY!" << endl;
        return 0;
    }

    unordered_map<int, int> sum_mask;
    int total = 1 << n;

    for (int mask = 1; mask < total; ++mask) {
        int sum = 0;
        for (int i = 0; i < n; ++i)
            if (mask & (1 << i))
                sum += a[i];

        if (sum_mask.count(sum)) {
            int other_mask = sum_mask[sum];
            if ((other_mask & mask) == 0) {
                cout << "YAY!" << endl;
                return 0;
            }
        } else {
            sum_mask[sum] = mask;
        }
    }

    cout << "AWW!" << endl;
    return 0;
}
