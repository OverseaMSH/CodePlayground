// https://quera.org/problemset/3558
#include <iostream>
#include <vector>
#include <algorithm> 
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    int nArr[10][2]; 
    int mArr[10][2];

    for (int i = 0; i < n; i++) {
        cin >> nArr[i][0] >> nArr[i][1];
    }

    for (int i = 0; i < m; i++) {
        cin >> mArr[i][0] >> mArr[i][1];
    }

    vector<int> nBig;
    vector<int> mBig;

    for (int i = 0; i < n; i++) {
        for (int j = nArr[i][0]; j <= nArr[i][1]; j++) {
            nBig.push_back(j);
        }
    }

    for (int i = 0; i < m; i++) {
        for (int j = mArr[i][0]; j <= mArr[i][1]; j++) {
            mBig.push_back(j);
        }
    }

    sort(nBig.begin(), nBig.end());
    sort(mBig.begin(), mBig.end());

    int commonCount = 0;
    size_t i = 0, j = 0;

    while (i < nBig.size() && j < mBig.size()) {
        if (nBig[i] < mBig[j]) {
            i++;
        } else if (nBig[i] > mBig[j]) {
            j++;
        } else { 
            commonCount++;
            i++;
            j++;
        }
    }

    cout  << commonCount << endl;

    return 0;
}