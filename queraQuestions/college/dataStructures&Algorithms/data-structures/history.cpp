// https://quera.org/college/3016/chapter/8242/lesson/27737/
#include <iostream>
#include <stack>
#include <vector>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<string> arr;
    stack<vector<string>> history;  

    for (int i = 0; i < n; i++) {
        string command;
        cin >> command;
        
        if (command == "insert") {
            int i;
            string value;
            cin >> i >> value;

            arr.insert(arr.begin() + i - 1, value);

            history.push(arr);
        } 
        else if (command == "delete") {
            int i;
            cin >> i;

            if (i <= arr.size()) {
                arr.erase(arr.begin() + i - 1);
                history.push(arr);
            }
        } 
        else if (command == "undo") {
            if (!history.empty()) {
                history.pop();
                if (!history.empty()) {
                    arr = history.top(); 
                } else {
                    arr.clear();  
                }
            }
        }
    }

    for (const auto& val : arr) {
        cout << val;
    }

    return 0;
}
