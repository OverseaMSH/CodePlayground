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
    d.push_back(L);  

    int currentPosition = 0;
    int fuelLeft = k;
    vector<int> stops;
    int lastStop = -1;

    for (int i = 0; i < d.size(); ) {
        if (d[i] - currentPosition > k) {
            if (lastStop == -1) {
                cout << -1 << endl;
                return 0;  
            }
            stops.push_back(lastStop); 
            currentPosition = d[lastStop];  
            fuelLeft = k;  
            lastStop = -1; 
        } else {
            lastStop = i; 
            i++; 
        }
    }

    cout << stops.size() << endl;  
    for (int stop : stops) {
        cout << stop + 1 << " ";  
    }
    cout << endl;

    return 0;
}
