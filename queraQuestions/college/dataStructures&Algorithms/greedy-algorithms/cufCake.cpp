//https://quera.org/college/3016/chapter/8236/lesson/60803
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> elems(n);
    for (int i = 0; i < n; i++) {
        cin >> elems[i];
    }

    if (k == 1) {
        cout << *max_element(elems.begin(), elems.end()) << endl;
    } else if (k == 2) {
        cout << min(elems[0], elems[n - 1]) << endl;
    } else if (k >= 3) {
        cout << *min_element(elems.begin(), elems.end()) << endl;
    }

    return 0;
}
