#include <bits/stdc++.h>
using namespace std;

int n;
vector<vector<int>> adj;

pair<int,int> bfs(int start){
    vector<int> dist(n+1, -1);
    queue<int> q;
    dist[start] = 0;
    q.push(start);

    int farthestNode = start;
    while(!q.empty()){
        int u = q.front(); q.pop();
        for(int v : adj[u]){
            if(dist[v] == -1){
                dist[v] = dist[u] + 1;
                q.push(v);
                if(dist[v] > dist[farthestNode]){
                    farthestNode = v;
                }
            }
        }
    }
    return {farthestNode, dist[farthestNode]};
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    adj.assign(n+1, {});

    for(int i=0;i<n-1;i++){
        int u,v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int A = bfs(1).first;

    int diameter = bfs(A).second;

    cout << diameter << "\n";
    return 0;
}
