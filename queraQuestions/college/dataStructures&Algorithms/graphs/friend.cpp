#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<vector<int>> adj(n+1);
    for(int i = 0; i < n-1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int q;
    cin >> q;
    vector<int> friends(q);
    for(int i = 0; i < q; i++) {
        cin >> friends[i];
    }

    // BFS from node 1
    vector<int> dist(n+1, -1);
    queue<int> bfs;
    dist[1] = 0;
    bfs.push(1);

    while(!bfs.empty()) {
        int u = bfs.front(); bfs.pop();
        for(int v : adj[u]) {
            if(dist[v] == -1) {
                dist[v] = dist[u] + 1;
                bfs.push(v);
            }
        }
    }

    int bestFriend = friends[0];
    int bestDist = dist[bestFriend];

    for(int i = 1; i < q; i++) {
        int f = friends[i];
        if(dist[f] < bestDist || (dist[f] == bestDist && f < bestFriend)) {
            bestFriend = f;
            bestDist = dist[f];
        }
    }

    cout << bestFriend << "\n";
    return 0;
}
