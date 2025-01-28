#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    int q;
    cin >> q;

    map<string, int> nameToId;
    vector<string> idToName;
    int nextId = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> dayHeap;
    priority_queue<int, vector<int>, greater<int>> customerHeap;
    vector<bool> marked;

    for (int day = 1; day <= q; ++day) {
        int k;
        cin >> k;

        for (int j = 0; j < k; ++j) {
            string name;
            int t;
            cin >> name >> t;

            if (nameToId.find(name) == nameToId.end()) {
                nameToId[name] = nextId++;
                idToName.push_back(name);
                marked.push_back(false);
            }

            int id = nameToId[name];
            int endDay = day + t - 1;

            dayHeap.push({endDay, id});
            customerHeap.push(id);
        }

        vector<string> toRemove;

        while (!dayHeap.empty() && dayHeap.top().first == day) {
            int id = dayHeap.top().second;
            dayHeap.pop();

            if (!marked[id]) {
                toRemove.push_back(idToName[id]);
                marked[id] = true;
            }
        }

        while (!customerHeap.empty() && marked[customerHeap.top()]) {
            customerHeap.pop();
        }

        if (!customerHeap.empty()) {
            int id = customerHeap.top();
            customerHeap.pop();
            toRemove.push_back(idToName[id]);
            marked[id] = true;
        }

        sort(toRemove.begin(), toRemove.end());

        for (const string& name : toRemove) {
            cout << name << " ";
        }
        cout << endl;
    }

    return 0;
}