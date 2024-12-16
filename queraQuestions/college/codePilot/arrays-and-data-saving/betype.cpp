// https://quera.org/college/4499/chapter/12639/lesson/42895/
#include <iostream>
#include <string>

using namespace std;

int main() {
    string input;
    cin >> input;

    string result = ""; 
    int index = 0;      

    for (char c : input) {
        if (c == '=') {
            if (index > 0) {
                --index; 
            }
        } else {
            if (index < result.size()) {
                result[index] = c; 
            } else {
                result += c; 
            }
            ++index; 
        }
    }

    cout << result.substr(0, index) << endl;

    return 0;
}
