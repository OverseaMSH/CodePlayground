// https://quera.org/problemset/168950
#include <iostream>
using namespace std;

int main() {
    string m;
    cin >> m;

    if (m == "december" || m == "january" || m == "february") {
        cout << "summer";
    } else if (m == "march" || m == "april" || m == "may") {
        cout << "autumn";
    } else if (m == "june" || m == "july" || m == "august") {
        cout << "winter";
    } else if (m == "september" || m == "october" || m == "november") {
        cout << "spring";
    } else {
        cout << "Invalid input!";
    }
    
    return 0;
}