#include <bits/stdc++.h>
using namespace std;

int getId(vector<int> &perm, vector<int> &fact) {
    int n = perm.size();
    int id = 0;
    vector<int> used(n+1, 0);
    for (int i = 0; i < n; i++) {
        int smaller = 0;
        for (int j = 1; j < perm[i]; j++) {
            if (!used[j]) smaller++;
        }
        id += smaller * fact[n - i - 1];
        used[perm[i]] = 1;
    }
    return id;
}

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    vector<int> fact(n+1, 1);
    for (int i = 1; i <= n; i++) fact[i] = fact[i-1] * i;

    int totalStates = fact[n];

    vector<int> dis(totalStates, -1);
    queue<vector<int>> q;

    int startId = getId(a, fact);
    dis[startId] = 0;
    q.push(a);

    vector<int> target(n);
    iota(target.begin(), target.end(), 1);
    int targetId = getId(target, fact);

    if (startId == targetId) {
        cout << 0;
        return 0;
    }

    while (!q.empty()) {
        auto perm = q.front(); q.pop();
        int currId = getId(perm, fact);
        int currDist = dis[currId];

        for (int x = 2; x <= n; x++) {
            auto newPerm = perm;
            reverse(newPerm.begin(), newPerm.begin() + x);
            int newId = getId(newPerm, fact);
            if (dis[newId] == -1) {
                dis[newId] = currDist + 1;
                if (newId == targetId) {
                    cout << dis[newId];
                    return 0;
                }
                q.push(newPerm);
            }
        }
    }

    return 0;
}
