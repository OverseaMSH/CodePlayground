// https://quera.org/college/3016/chapter/8244/lesson/65231/?comments_page=1&comments_filter=ALL&submissions_page=1
#include <bits/stdc++.h>

using namespace std;

const int MAXN = 100005;

vector<int> adj[MAXN];
vector<int> dist(MAXN, -1);  
vector<int> parent(MAXN, -1); 
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

    queue<int> q;
    q.push(s);
    dist[s] = 0;

    while (!q.empty()) {
        int v = q.front();
        q.pop();

        for (int u : adj[v]) {
            if (dist[u] == -1) {
                dist[u] = dist[v] + 1;
                parent[u] = v;
                q.push(u);
            }
        }
    }

    if (dist[t] == -1) {
        cout << -1 << '\n';
    } else {
        cout << dist[t] << '\n';

        vector<int> path;
        for (int v = t; v != -1; v = parent[v]) {
            path.push_back(v);
        }
        reverse(path.begin(), path.end());

        for (int v : path)
            cout << v << ' ';
        cout << '\n';
    }

    return 0;
}
