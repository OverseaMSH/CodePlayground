#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<long long>> a(n, vector<long long>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a[i][j];
        }
    }

    long long maxSum = LLONG_MIN;
    for (int r1 = 0; r1 < n; r1++) {
        vector<long long> temp(m, 0); 
        for (int r2 = r1; r2 < n; r2++) {
            for (int j = 0; j < m; j++) {
                temp[j] += a[r2][j];
            }

            long long currentSum = 0;
            long long bestSum = LLONG_MIN;
            for (long long val : temp) {
                currentSum = max(val, currentSum + val);
                bestSum = max(bestSum, currentSum);
            }

            maxSum = max(maxSum, bestSum);
        }
    }

    cout << maxSum << endl;
    return 0;
}
