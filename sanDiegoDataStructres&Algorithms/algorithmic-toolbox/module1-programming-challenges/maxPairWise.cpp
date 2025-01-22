#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int MaxPairwiseProduct(const vector<int>& numbers) {
    int n = numbers.size();
    if (n < 2) {
        return 0; 
    }

    int first_max = max(numbers[0], numbers[1]);
    int second_max = min(numbers[0], numbers[1]);

    for (int i = 2; i < n; ++i) {
        if (numbers[i] > first_max) {
            second_max = first_max;
            first_max = numbers[i];
        } else if (numbers[i] > second_max) {
            second_max = numbers[i];
        }
    }

    return first_max * second_max;
}

int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }
    cout << MaxPairwiseProduct(numbers) << "\n";
    return 0;
}
