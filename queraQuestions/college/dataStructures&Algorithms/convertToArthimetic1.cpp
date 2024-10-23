// https://quera.org/college/3016/chapter/10131/lesson/60773/?comments_page=1&comments_filter=ALL&submissions_page=1
#include <iostream>
#include <cmath>  
#include <algorithm> 
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    int arr[100]; 
    int m = 100, M = -100;  
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        m = min(m, arr[i]);  
        M = max(M, arr[i]); 
    }

    int ans = 1e9; 

    for (int x = m - (n - 1) * k; x <= M; x++) {
        int cost = 0;

        for (int i = 0; i < n; i++) {
            int bi = x + i * k; 
            cost += abs(bi - arr[i]);  
        }

        ans = min(ans, cost);
    }

    cout << ans << endl;

    return 0;
}
