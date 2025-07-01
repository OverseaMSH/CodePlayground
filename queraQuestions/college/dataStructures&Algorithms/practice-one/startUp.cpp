#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> chocolates(4);
    vector<int> eaten(4, 0);
    for (int i = 0; i < 4; i++)
        cin >> chocolates[i];

    int rotation = 0; // تعداد چرخش ظرف
    int turn = 0;     // نوبت نفرها (0 تا 3)

    while (true) {
        int idx = (turn - rotation + 4) % 4; // بخش روبروی نفر turn

        if (chocolates[idx] == 0)
            break;

        eaten[turn]++;
        chocolates[idx]--;

        rotation = (rotation + 1) % 4; // چرخش ۹۰ درجه خلاف عقربه‌های ساعت
        turn = (turn + 1) % 4;         // نفر بعدی
    }

    for (int i = 0; i < 4; i++)
        cout << eaten[i] << " ";
    cout << "\n";

    return 0;
}
