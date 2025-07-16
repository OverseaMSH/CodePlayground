// https://quera.org/college/3016/chapter/8244/lesson/65232/?comments_page=1&comments_filter=ALL&submissions_page=1
#include <bits/stdc++.h>

using namespace std;

const int MAXN = 100005;
vector<int> adj[MAXN]; 
vector<bool> visited(MAXN, false);

void dfs(int node) {
    visited[node] = true;
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor);
        }
    }
}

int main() {


    int n, m;
    cin >> n >> m;

    int s, t;
    cin >> s >> t;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u); 
    }

    dfs(s);

    if (visited[t])
        cout << "YES\n";
    else
        cout << "NO\n";

    return 0;
}
