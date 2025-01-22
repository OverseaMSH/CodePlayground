// https://quera.org/college/4499/chapter/12640/lesson/42910/
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int n, s, t;
    cin >> n;
    string houses;
    cin >> houses;
    cin >> s >> t;

    if (s > t) swap(s, t);
    string path = houses.substr(s - 1, t - s + 1);

    vector<int> blocks;
    int count = 0;
    for (char c : path) {
        if (c == 'H') {
            count++;
        } else {
            if (count > 0) blocks.push_back(count);
            count = 0;
        }
    }
    if (count > 0) blocks.push_back(count);

    auto count_operations = [](int size) {
        return __builtin_popcount(size);
    };

    int result = 0;
    for (int block : blocks) {
        result += count_operations(block);
    }

    cout << result << endl;
    return 0;
}
