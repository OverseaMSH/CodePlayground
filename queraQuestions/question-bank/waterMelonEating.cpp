// https://quera.org/problemset/35253
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    int weights[n], indices[n];

    for (int i = 0; i < n; i++) {
        cin >> weights[i];
        indices[i] = i + 1;  
    }

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (weights[i] > weights[j]) {
                swap(weights[i], weights[j]);
                swap(indices[i], indices[j]);
            }
        }
    }

    cout << indices[n - 1] << endl;

    return 0;
}
