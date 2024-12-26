#include <iostream>
#include <vector>
#include <string>
#include <algorithm>  
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> arr(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    vector<vector<int>> dp(n, vector<int>(m, 0));
    vector<vector<char>> direction(n, vector<char>(m, ' '));

    dp[n - 1][0] = arr[n - 1][0];

    for (int i = n - 1; i >= 0; i--) {
        for (int j = 0; j < m; j++) {
            if (i < n - 1) {
                if (dp[i][j] < dp[i + 1][j] + arr[i][j]) {
                    dp[i][j] = dp[i + 1][j] + arr[i][j];
                    direction[i][j] = 'U'; 
                    
                }
            }
            if (j > 0) {
                if (dp[i][j] < dp[i][j - 1] + arr[i][j]) {
                    dp[i][j] = dp[i][j - 1] + arr[i][j];
                    direction[i][j] = 'R'; 
                }
            }
        }
    }

    cout << dp[0][m - 1] << endl;

    string path;
    int i = 0, j = m - 1;
    while (i != n - 1 || j != 0) {
        if (direction[i][j] == 'U') {
            path += 'U';
            i++;
        } else if (direction[i][j] == 'R') {
            path += 'R';
            j--;
        }
    }

    reverse(path.begin(), path.end()); 
    cout << path << endl;

    return 0;
}
