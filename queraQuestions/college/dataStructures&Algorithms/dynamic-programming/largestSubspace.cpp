https://quera.org/college/3016/chapter/8238/lesson/27724
#include <iostream>
#include <algorithm> 
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    long long maxSum = arr[0];
    long long currentSum = arr[0];

    for (int i = 1; i < n; i++) {
        currentSum = max((long long)arr[i], currentSum + arr[i]);
        maxSum = max(maxSum, currentSum);
    }

    cout << maxSum << endl;
    return 0;
}
