#include <iostream>
#include <list>
#include <string>

using namespace std;

int main() {
    int q;
    cin >> q;
    
    list<char> text;
    auto cursor = text.begin();  

    while (q--) {
        string command;
        cin >> command;

        if (command == "+") {
            if (cursor != text.end()) {
                cursor++;
            }
        } 
        else if (command == "-") {
            if (cursor != text.begin()) {
                cursor--;
            }
        } 
        else if (command == "insert") {
            char c;
            cin >> c;
            text.insert(cursor, c);  
        }
    }

    string result(text.begin(), text.end());
    cout << result << endl;

    return 0;
}
