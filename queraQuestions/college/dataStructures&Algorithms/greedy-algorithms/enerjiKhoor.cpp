// https://quera.org/college/3016/chapter/8236/lesson/28702
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    long long k; 
    cin >> n >> k;

    vector<pair<long long, long long>> fruits;
    for (int i = 0; i < n; i++) {
        long long b, a;
        cin >> b >> a;
        fruits.push_back({b, a});
    }

    sort(fruits.begin(), fruits.end());

    long long max_energy = k; 
    for (const auto& fruit : fruits) {
        long long b = fruit.first; 
        long long a = fruit.second; 

        if (k >= b && b < a) {
            k += a - b;    
            max_energy = max(max_energy, k);
        }
    }

    cout << max_energy << endl;

    return 0;
}
