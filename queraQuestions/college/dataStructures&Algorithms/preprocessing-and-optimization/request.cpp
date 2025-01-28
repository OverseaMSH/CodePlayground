#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    
    vector<vector<int>> sets(n + 1);
    
    for (int i = 1; i <= n; ++i) {
        sets[i].push_back(i);
    }
    
    for (int i = 0; i < q; ++i) {
        int type;
        cin >> type;
        
        if (type == 1) {
            int a, b;
            cin >> a >> b;
            
            sets[b].insert(sets[b].end(), sets[a].begin(), sets[a].end());
            
            sets[a].clear();
        } else if (type == 2) {
            int c;
            cin >> c;
            
            cout << sets[c].size() << endl;
        } else if (type == 3) {
            int d;
            cin >> d;
            
            if (sets[d].empty()) {
                cout << -1 << endl;
            } else {
                sort(sets[d].begin(), sets[d].end());
                for (int num : sets[d]) {
                    cout << num << " ";
                }
                cout << endl;
            }
        }
    }
    
    return 0;
}