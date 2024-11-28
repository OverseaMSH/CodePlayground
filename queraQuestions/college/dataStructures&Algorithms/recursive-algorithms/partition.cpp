// https://quera.org/college/3016/chapter/8235/lesson/27774/
#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<long long> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    long long totalSum = accumulate(arr.begin(), arr.end(), 0LL); 
    long long minDiff = totalSum; 
    for (int mask = 0; mask < (1 << n); mask++) {
        long long subsetSum = 0;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) { 
                subsetSum += arr[i];
            }
        }
        long long otherSum = totalSum - subsetSum;
        minDiff = min(minDiff, abs(subsetSum - otherSum));
    }

    cout << minDiff << endl;
    return 0;
}
