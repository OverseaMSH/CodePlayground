// https://quera.org/college/3016/chapter/8240/lesson/29199/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll merge(vector<int>& arr, int left, int mid, int right) {
    int d1 = mid - left;
    int d2 = right - mid;
    vector<int> leftArr(arr.begin() + left, arr.begin() + mid);
    vector<int> rightArr(arr.begin() + mid, arr.begin() + right);

    ll counter = 0;
    int i = 0, j = 0, k = left;
    while (i < d1 && j < d2) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k++] = leftArr[i++];
        } else {
            arr[k++] = rightArr[j++];
            counter += d1 - i; 
        }
    }
    while (i < d1) arr[k++] = leftArr[i++];
    while (j < d2) arr[k++] = rightArr[j++];
    return counter;
}

ll counter(vector<int>& arr, int left, int right) {
    if (right - left <= 1) return 0;

    int mid = (left + right) / 2;
    ll result = 0;
    result += counter(arr, left, mid);
    result += counter(arr, mid, right);
    result += merge(arr, left, mid, right);

    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n); 
    for (int i = 0; i < n; ++i)
        cin >> arr[i];

    cout << counter(arr, 0, n) << endl;
    return 0;
}
