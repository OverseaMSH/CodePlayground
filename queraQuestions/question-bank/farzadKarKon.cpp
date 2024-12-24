// https://quera.org/problemset/658
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    
    for (int i = 0; i < n; i++) {
        cin >> arr[i]; 
    }
    
    int current_sum = 0; 
    int max_sum = 0; 
    
    for (int i = 0; i < n; i++) {
        current_sum += arr[i]; 
        if (current_sum < 0) {
            current_sum = 0; 
        }
        max_sum = max(max_sum, current_sum); 
    }
    
    cout << max_sum << endl;
    return 0;
}
