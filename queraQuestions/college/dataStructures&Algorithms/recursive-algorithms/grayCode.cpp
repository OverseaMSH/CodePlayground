#include <iostream>
#include <vector>
#include <string>
using namespace std;

// تابع بازگشتی برای تولید کد گری
vector<string> generateGrayCode(int length) {
    // حالت پایه: اگر طول صفر باشد، لیست خالی را برگردان
    if (length == 0) {
        return {""}; // فقط یک کد خالی
    }

    // کد گری برای طول قبلی
    vector<string> G1 = generateGrayCode(length - 1);

    // کپی معکوس G1 برای G2
    vector<string> G2(G1.rbegin(), G1.rend());

    // افزودن '0' به ابتدای همه عناصر G1
    for (string &code : G1) {
        code = "0" + code;
    }

    // افزودن '1' به ابتدای همه عناصر G2
    for (string &code : G2) {
        code = "1" + code;
    }

    // ترکیب G1 و G2
    G1.insert(G1.end(), G2.begin(), G2.end());

    return G1;
}

int main() {
    int n;
    cout << "Enter the length of Gray code: ";
    cin >> n;

    vector<string> grayCode = generateGrayCode(n);

    // نمایش کد گری
    for (const string &code : grayCode) {
        cout << code << endl;
    }

    return 0;
}
