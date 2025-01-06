#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> a(n); 
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        --a[i];
    }
    
    vector<int> counter(n, 0);
    for (int i = 0; i < n; ++i) {
        counter[a[i]]++;
    }
    
    queue<int> q;
    for (int i = 0; i < n; ++i) {
        if (counter[i] == 0) {
            q.push(i);
        }
    }
    
    vector<bool> visited(n, false);
    while (!q.empty()) {
        int x = q.front();
        q.pop();
        
        if (!visited[x]) {
            visited[x] = true;
            counter[a[x]]--;
            
            if (counter[a[x]] == 0) {
                q.push(a[x]);
            }
        }
    }
    
    vector<int> result;
    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            result.push_back(i + 1); 
        }
    }
    
    sort(result.begin(), result.end());
    
    cout << result.size() << endl;
    for (int i = 0; i < result.size(); ++i) {
        cout << result[i] << " ";
    }
    cout << endl;
    
    return 0;
}
