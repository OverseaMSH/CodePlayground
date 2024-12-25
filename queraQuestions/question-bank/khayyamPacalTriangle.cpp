// https://quera.org/problemset/595
#include <iostream>

using namespace std;

void generatePascalTriangle(int n) {
    int triangle[n][n];
    for (int i = 0; i < n; i++) {
        triangle[i][0] = triangle[i][i] = 1;
        for (int j = 1; j < i; j++) {
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cout << triangle[i][j] << ' ';
        }
        cout << endl;
    }
}

int main() {
    int n;
    cin >> n;
    generatePascalTriangle(n);
    return 0;
}