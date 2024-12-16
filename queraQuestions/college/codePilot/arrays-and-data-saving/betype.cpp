// https://quera.org/college/4499/chapter/12639/lesson/42895/
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    string input;
    cin >> input;

    vector<char> charArray(input.begin(), input.end());

    for (size_t i = 0; i < charArray.size(); ++i) {
        if (charArray[i] == '=') {
            charArray.erase(charArray.begin() + i);
            charArray.erase(charArray.begin() + (i - 1));
            if (i > 0) {
                
                i-=2;
            }
        }
    }

    for (char c : charArray) {
        cout << c;
    }
    cout << endl;

    return 0;
}
