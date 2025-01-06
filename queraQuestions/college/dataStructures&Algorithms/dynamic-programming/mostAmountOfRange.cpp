#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<int, int>> intervals(n);
    
    for (int i = 0; i < n; ++i) {
        cin >> intervals[i].first >> intervals[i].second;
    }
    
    sort(intervals.begin(), intervals.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second < b.second;
    });

    int lastR = -1; 
    int count = 0; 

    // انتخاب بازه‌ها
    for (const auto& interval : intervals) {
        if (lastR <= interval.first) {  
            lastR = interval.second;    
            count++;                    
        }
    }

    cout << count << endl;

    return 0;
}
