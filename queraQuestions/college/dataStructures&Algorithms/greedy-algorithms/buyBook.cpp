// https://quera.org/college/3016/chapter/8236/lesson/167525
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxBooks(int n, long long r, vector<int>& prices) {
    sort(prices.begin(), prices.end());
    
    int count = 0;  
    long long remainingMoney = r; 
    
    for (int price : prices) {
        if (remainingMoney >= price) {
            count++; 
            remainingMoney -= price;  
        } else {
            break;  
        }
    }
    
    return count;
}

int main() {
    int n;
    long long r;
    cin >> n >> r;
    
    vector<int> prices(n);
    
    for (int i = 0; i < n; ++i) {
        cin >> prices[i];
    }
    
    cout << maxBooks(n, r, prices) << endl;
    
    return 0;
}
