#include <bits/stdc++.h>
using namespace std;

int n;
vector<vector<long long>> h;
vector<vector<bool>> visited;

int dx[8] = {-1,-1,-1,0,0,1,1,1};
int dy[8] = {-1,0,1,-1,1,-1,0,1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    h.assign(n, vector<long long>(n));
    visited.assign(n, vector<bool>(n,false));

    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            cin >> h[i][j];

    int peakCount = 0, valleyCount = 0;

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(visited[i][j]) continue;

            long long height = h[i][j];
            bool hasHigher = false, hasLower = false;

            // BFS to find the block
            queue<pair<int,int>> q;
            q.push({i,j});
            visited[i][j] = true;

            while(!q.empty()){
                auto [x,y] = q.front(); q.pop();

                for(int d=0; d<8; d++){
                    int nx = x+dx[d], ny = y+dy[d];
                    if(nx<0 || ny<0 || nx>=n || ny>=n) continue;

                    if(h[nx][ny]==height && !visited[nx][ny]){
                        visited[nx][ny] = true;
                        q.push({nx,ny});
                    } else if(h[nx][ny] != height) {
                        if(h[nx][ny] > height) hasHigher = true;
                        if(h[nx][ny] < height) hasLower = true;
                    }
                }
            }

            if(!hasHigher) peakCount++;
            if(!hasLower) valleyCount++;
        }
    }

    cout << peakCount << " " << valleyCount << "\n";
    return 0;
}
