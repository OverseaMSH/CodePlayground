#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Phone {
    int price, quality;
};

bool comparePhones(const Phone &a, const Phone &b) {
    if (a.price == b.price)
        return a.quality > b.quality;
    return a.price < b.price;
}

int main() {
    int n;
    cin >> n;
    vector<Phone> phones(n);

    for (int i = 0; i < n; ++i) {
        cin >> phones[i].price >> phones[i].quality;
    }

    sort(phones.begin(), phones.end(), comparePhones);

    int count = 0; 
    int max_quality = 0;

    for (const auto &phone : phones) {
        if (phone.quality > max_quality) {
            ++count;  
            max_quality = phone.quality; 
        }
    }

    cout << count << endl;

    return 0;
}
