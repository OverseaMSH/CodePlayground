#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, c;
    cin >> n >> c;

    vector<int> x(n);
    for (int i = 0; i < n; i++) {
        cin >> x[i];
    }

    sort(x.begin(), x.end(), greater<int>());

    for (int i = 0; i < n; i++) {
        int d = min(c, max(0, x[i] - c)); 
        c -= d;  
    }

    cout << c << endl; 
    return 0;
}
