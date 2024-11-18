#include <iostream>
#include <vector>
using namespace std;

void purgeList(vector<int>& arr) {
    for (size_t p = 0; p < arr.size(); p++) {
        size_t q = p + 1; 
        while (q < arr.size()) {
            if (arr[p] == arr[q]) {
                arr.erase(arr.begin() + q); 
            } else {
                q++; 
            }
        }
    }
}

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    purgeList(arr);

    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
