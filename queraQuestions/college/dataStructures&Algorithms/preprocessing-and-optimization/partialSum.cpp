#include <iostream>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;

    long long arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    long long partialSum[n + 1]; 
    partialSum[0] = 0;
    for (int i = 1; i <= n; i++)
        partialSum[i] = partialSum[i - 1] + arr[i - 1];

    for (int i = 0; i < q; i++) {
        int l, r;
        cin >> l >> r;
        cout << partialSum[r + 1] - partialSum[l] << endl;
    }

    return 0;
}
