// https://quera.org/problemset/17902
#include <iostream>
#include <string>
using namespace std;

int main() {
    int k;
    cin >> k;
    string pass;
    cin >> pass;
    int sum = 0;
    for (int i = 0; i < k; i++) {
        string n;
        cin >> n;
        int j = 0;
        while (n[j] != pass[i]) {
            j++;
        }
        sum += min(j, 9 - j);
    }
    cout << sum << endl;
    return 0;
}
