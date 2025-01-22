// https://quera.org/college/3016/chapter/8235/lesson/27765
#include <iostream>
#include <vector>
using namespace std;

void generate(vector<int>& arr, int n) {
    if (arr.size() == n) {
        for (int i = 0; i < arr.size(); i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
        return;
    }

    for (int i = 1; i <= n; i++) {
        arr.push_back(i); 
        generate(arr, n); 
        arr.pop_back();   
    }
}

int main() {
    int n;
    cin >> n;

    vector<int> arr; 
    generate(arr, n); 

    return 0;
}

