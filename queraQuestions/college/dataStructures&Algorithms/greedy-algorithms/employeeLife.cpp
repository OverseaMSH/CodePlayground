https://quera.org/college/3016/chapter/8236/lesson/27786/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long max(long long n, vector<long long>& arr) {
    sort(arr.begin(), arr.end());
    long long counter=0;
    for(int i=0;i<n;i++){
        if(counter<arr[i]){
            counter++;
        }
    }
    return counter;
}

int main() {
    long long n;
    cin >> n;
    
    vector<long long> arr(n);
    
    for (long long i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    
    cout << max(n, arr) << endl;
    
    return 0;
}
