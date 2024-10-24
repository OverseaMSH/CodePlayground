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

    for (int j = 1; j <= n; j++) { 
        for (int i = 1; i <= n - j; i++) { 
            if (arr[i - 1] > arr[i]) { 
                swap(arr[i - 1], arr[i]);
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl; 

    return 0;
}