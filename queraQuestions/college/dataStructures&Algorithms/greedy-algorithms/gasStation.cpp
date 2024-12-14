#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, k, L;
    cin >> n >> k >> L;
    vector<int> d(n);
    for (int i = 0; i < n; i++) {
        cin >> d[i];
    }

    d.push_back(L); // افزودن هدف (L) به لیست پمپ‌ها.

    int currentPosition = 0;
    int fuelLeft = k;  
    vector<int> stops; // برای نگهداری ایندکس پمپ‌های انتخاب شده.
    int lastStop = -1;  

    for (int i = 0; i < d.size(); i++) {
        // چک کنید آیا می‌توان به پمپ فعلی رسید.
        if (d[i] - currentPosition > fuelLeft) {
            // نمی‌توان به این پمپ دسترسی داشت، پس باید از آخرین پمپ سوخت‌گیری کنیم.
            if (lastStop == -1) {
                cout << -1 << endl;
                return 0; // نمی‌توان سفر کرد.
            }
            stops.push_back(lastStop + 1); // ایندکس را نشان می‌دهیم. به خاطر i=0 باید 1 اضافه کنیم.
            currentPosition = d[lastStop]; // به آخرین ایستگاه بروید.
            fuelLeft = k; // باک را پر کنید.
            fuelLeft -= (d[lastStop] - currentPosition); // سوخت را به روز کنید.
        }

        // سوخت را به روز کنید.
        fuelLeft -= (d[i] - currentPosition);
        currentPosition = d[i];
        lastStop = i; // آخرین ایستگاه که در آن توقف کردید را جلوی دست نگه‌دارید.
    }

    // نتیجه را چاپ کنید.
    cout << stops.size() << endl;
    for (int stop : stops) {
        cout << stop << " "; // ایندکس باید بر اساس 1 شروع شود.
    }
    cout << endl;

    return 0;
}