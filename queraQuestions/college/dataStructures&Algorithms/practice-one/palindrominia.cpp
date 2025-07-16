// https://quera.org/college/3016/chapter/8237/lesson/29955/?comments_page=1&comments_filter=ALL&submissions_page=1
#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

const int MOD = 1e9 + 7;

bool is_palindrome3(char a, char b, char c) {
    return a == c;
}

int main() {
    string s;
    cin >> s;
    int n = s.size();

    unordered_map<string, int> dp_curr, dp_next;
    dp_curr["**"] = 1;  

    for (int i = 0; i < n; ++i) {
        char ch = s[i];
        dp_next.clear();

        for (auto& entry : dp_curr) {
            string last2 = entry.first;
            int count = entry.second;

            for (char c : (ch == '?' ? string("ab") : string(1, ch))) {
                char prev1 = last2[0];
                char prev2 = last2[1];

                if (i >= 2 && is_palindrome3(prev1, prev2, c)) continue;

                string next2 = {prev2, c};
                dp_next[next2] = (dp_next[next2] + count) % MOD;
            }
        }

        dp_curr.swap(dp_next); 
    }

    int result = 0;
    for (auto& entry : dp_curr) {
        result = (result + entry.second) % MOD;
    }

    cout << result << endl;
    return 0;
}
