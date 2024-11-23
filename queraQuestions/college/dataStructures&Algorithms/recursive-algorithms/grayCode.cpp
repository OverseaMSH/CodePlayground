#include <iostream>
#include <vector>
#include <string>

using namespace std;

string intToBin(int num, int size) {
    string bin = "";
    for (int i = size - 1; i >= 0; i--) {
        bin += (num & (1 << i)) ? '1' : '0';
    }
    return bin;
}

std::vector<int> generateGrayCode(int n) {
    int len = 1 << n;
    std::vector<int> grayCode;

    for (int i = 0; i < len; i++) {
        grayCode.push_back(i ^ (i >> 1));
    }

    return grayCode;
}

int main() {
    int n;
    cin >> n;
    vector<int> grayCode = generateGrayCode(n);
    for (int gc : grayCode) {
        cout << intToBin(gc, n) << endl;
    }
    return 0;
}
