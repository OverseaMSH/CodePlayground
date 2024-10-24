#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    long long n;
    cin >> n;
    vector<long long> a(n);
    
    for (long long i = 0; i < n; i++) {
        cin >> a[i];
    }

    vector<long long> newA = a;
    sort(newA.begin(), newA.end());

    int counter = 0;
    for (long long i = 0; i < n; i++) {
        if (a[i] != newA[i]) {
            counter++;
        }
    }

    if (counter == 2) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}
