//https://quera.org/college/3016/chapter/8236/lesson/167532
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>


using namespace std;

int main() {
    long long n, v; 
    cin >> n >> v;
    vector<pair<long long, long long>> juicePair;
    
    for (int i = 0; i < n; i++) {
        long long hi, vi;
        cin >> hi >> vi; 
        juicePair.push_back({hi, vi});
    }

    sort(juicePair.begin(), juicePair.end(), [](const pair<long long, long long>& a, const pair<long long, long long>& b) {
        return (double)a.first / a.second > (double)b.first / b.second;
    });

    long double result = 0;
    for (const auto& juice : juicePair) {
        if (v <= 0) break; 
        if (juice.second <= v) {
            result += juice.first;
            v -= juice.second;
        } else {
            result += (long double)v / juice.second * juice.first;
            v = 0; 
        }
    }

     cout <<fixed <<setprecision(3)<<result;

    return 0;
}
