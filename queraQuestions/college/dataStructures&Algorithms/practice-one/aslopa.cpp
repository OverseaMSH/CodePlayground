// https://quera.org/college/3016/chapter/8237/lesson/29743/
#include <iostream>
#include <cmath>
using namespace std;

int countWays(int x, int n, int current) {
    int p = (int)pow(current, n);
    if (p > x) return 0;
    if (p == x) return 1;

    return countWays(x - p, n, current + 1) + countWays(x, n, current + 1);
}

int main() {
    int x, n;
    cin >> x >> n;
    cout << countWays(x, n, 1) << endl;
    return 0;
}
