// https://quera.org/college/3016/chapter/10131/lesson/60773/?comments_page=1&comments_filter=ALL&submissions_page=1
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath> 

using namespace std;

int main() {
    long long n, k;
    cin >> n >> k;

    vector<long long> a(n);
    for (long long i = 0; i < n; i++) {
        cin >> a[i];
    }

    vector<long long> b(n);
    for (long long i = 0; i < n; i++) {
        b[i] = a[i] - i * k; 
    }

    sort(b.begin(), b.end());

    long long median;
    if (n % 2 == 0) {
        median = b[n / 2 - 1]; 
    } else {
        median = b[n / 2]; 
    }

    long long cost = 0;
    for (long long i = 0; i < n; i++) {
        cost += abs(b[i] - median);
    }

    cout << cost << endl;
    return 0;
}

