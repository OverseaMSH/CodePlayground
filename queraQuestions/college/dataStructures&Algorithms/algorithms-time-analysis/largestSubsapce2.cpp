#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    long long maxSum = arr[0]; 
    for (int i = 0; i < n; i++) {
        long long sum = 0;
        for (int j = i; j < n; j++) {
            sum += arr[j]; 
            if (sum > maxSum) {
                maxSum = sum;
            }
        }
    }

    cout << maxSum << endl;
    return 0;
}
