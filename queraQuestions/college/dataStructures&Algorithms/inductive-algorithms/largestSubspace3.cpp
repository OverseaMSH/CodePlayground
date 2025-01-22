#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> arr(n); 
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    long long ans = arr[0]; 
    long long maxsum = arr[0]; 
    for (int i = 1; i < n; i++) {
        maxsum = max(maxsum + arr[i], (long long)arr[i]);
        ans = max(ans, maxsum);
    }

    cout << ans << endl; 
    return 0;
}