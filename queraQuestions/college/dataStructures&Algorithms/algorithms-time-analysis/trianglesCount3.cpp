#include <iostream>
#include <algorithm>
using namespace std;

int main() {
int n;
cin >> n;
int counter = 0;

for (int a = 1; a <= n / 3; a++) {
int max_value = max(0, (n / 2) - (2 * a) + 1);
counter += ((n - (3 * a)) / 2) - max_value + 1;
}

cout << counter << endl;
return 0;
}