#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    
    vector<int> arr1(n);
    for (int i = 0; i < n; i++) {
        cin >> arr1[i];
    }

    int m = 0;
    for (int i = 0; i < n; i++) {
        if (arr1[i] > m) {
            m = arr1[i];
        }
    }

    vector<int> cnt(m + 1, 0); 
    for (int i = 0; i < n; i++) {
        cnt[arr1[i]]++;
    }

    vector<int> ps(m + 1, 0);
    for (int i = 1; i <= m; i++) {
        ps[i] = ps[i - 1] + cnt[i];
    }

    for (int i = 0; i < q; i++) {
        int x;
        cin >> x;

        if (x > m) {
            cout << n << endl; 
        } else {
            cout << ps[x - 1] << endl; 
        }
    }

    return 0;
}