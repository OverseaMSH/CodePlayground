// https://quera.org/college/4499/chapter/12637/lesson/42865
#include <iostream>
using namespace std;

int main() {
    int x1, y1, x2, y2, x3, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
    cout << (x1 ^ x2 ^ x3) << " " << (y1 ^ y2 ^ y3);
    return 0;
}
