#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    if (b >= a) {
        cout << "Wrong order!" << endl;
    }
    else if ((a - b) % 2 != 0) {
        cout << "Wrong difference!" << endl;
    }
    else {
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < a; j++) {
                if (i > ((a-b)/2)-1 && j >((a-b)/2)-1 && i < (a-(a-b)/2) && j < (a-(a-b)/2) ) {
                    cout << "  ";
                } else {
                    cout << "* ";
                }
            }
            cout << endl;
        }
    }

    return 0;
}
