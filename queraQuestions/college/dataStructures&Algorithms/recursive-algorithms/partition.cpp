#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int totalSum = accumulate(arr.begin(), arr.end(), 0);
    int minDiff = totalSum; 
    for (int mask = 0; mask < (1 << n); mask++) {
        int subsetSum = 0;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) { 
                subsetSum += arr[i];
            }
        }
        int otherSum = totalSum - subsetSum;
        minDiff = min(minDiff, abs(subsetSum - otherSum));
    }

    cout << minDiff << endl;
    return 0;
}
