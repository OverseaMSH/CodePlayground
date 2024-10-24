#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n; 
    long long counter = 0; 

    for (int a = 1; a <= n / 3; a++) {
        int lower_bound = max(0, (n / 2) - (2 * a) + 1); 
        int upper_bound = (n - (3 * a)) / 2;
        if (lower_bound <= upper_bound) {
            counter += (upper_bound - lower_bound + 1); 
        }
    }

    cout << counter << endl;
    return 0; 
}
