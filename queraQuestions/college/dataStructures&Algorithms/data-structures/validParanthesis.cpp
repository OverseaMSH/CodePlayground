// https://quera.org/college/3016/chapter/8242/lesson/27736/
#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    string s;
    cin >> s;
    
    stack<int> parans; 
    vector<pair<int, int>> result;
    
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(') {
            parans.push(i); 
        } else if (s[i] == ')') {
            if (!parans.empty()) {
                int openIndex = parans.top();
                parans.pop();
                result.push_back({openIndex + 1, i + 1}); 
            } else {
                cout << -1 << endl;
                return 0;
            }
        }
    }
        if (!parans.empty()) {
        cout << -1 << endl;
        return 0;
    }
    
    sort(result.begin(), result.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second < b.second;
    });
    
    for (const auto& p : result) {
        cout << p.first << " " << p.second << endl;
    }
    
    return 0;
}
