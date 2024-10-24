// https://quera.org/college/3016/chapter/10131/lesson/146597/?comments_page=1&comments_filter=ALL&submissions_page=1
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);  

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());

    int mid;
    if (n % 2 == 0) {
        mid = arr[(n / 2) - 1];  
    } else {
        mid = arr[n / 2];  
    }

    long long op = 0;  
    for (int i = 0; i < n; i++) {
        op += abs(arr[i] - mid);
    }
    cout << mid << " " << op << endl;

    return 0;
}
