#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    vector<int> arr;
    string s[5];
    
    for (int i = 0; i < 5; i++) {
        getline(cin, s[i]);
    }

    for (int i = 0; i < 5; i++) {
        for (size_t j = 0; j < s[i].size(); j++) {
            if (s[i][j] == 'M') {
                if (s[i].substr(j, 6) == "MOLANA") {
                    arr.push_back(i + 1);
                    break;
                }
            } else if (s[i][j] == 'H') {
                if (s[i].substr(j, 5) == "HAFEZ") {
                    arr.push_back(i + 1);
                    break;
                }
            }
        }
    }

    if (arr.empty()) {
        cout << "NOT FOUND!" << endl;
    } else {
        for (size_t i = 0; i < arr.size(); i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }

    return 0;
}
