#https://quera.org/college/3016/chapter/8236/lesson/28702/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    long long k; // تبدیل k به long long
    cin >> n >> k;

    vector<pair<long long, long long>> v; // تبدیل مقادیر a و b به long long
    for (int i = 0; i < n; i++) {
        long long a, b;
        cin >> a >> b;
        v.push_back({a, b});
    }

    // مرتب‌سازی بر اساس مقدار دوم
    sort(v.begin(), v.end(), [](const pair<long long, long long>& p1, const pair<long long, long long>& p2) {
        return p1.first < p2.first;
    });

    // محاسبه k
    for (auto p : v) {
        if (p.second > p.first) {
            k += p.second - p.first;
        }
    }

    cout << k << endl; // چاپ مقدار نهایی k

    return 0;
}
