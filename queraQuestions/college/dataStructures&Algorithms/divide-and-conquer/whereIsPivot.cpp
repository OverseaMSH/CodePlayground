#include <iostream>
#include <vector>
using namespace std;

void quicksort(vector<int>& a, int l, int r, vector<int>& pivots) {
    if (l >= r) return;

    int pivot = a[l];
    pivots.push_back(pivot);

    int i = l + 1;
    for (int j = l + 1; j <= r; ++j) {
        if (a[j] < pivot) {
            swap(a[i], a[j]);
            ++i;
        }
    }

    swap(a[l], a[i - 1]);

    quicksort(a, l, i - 2, pivots); 
    quicksort(a, i, r, pivots);     
}

int main() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    vector<int> pivots;
    quicksort(a, 0, n - 1, pivots);

    for (int i = 0; i < pivots.size(); ++i) {
        cout << pivots[i];
        if (i < pivots.size() - 1)
            cout << ' ';
    }
    cout << endl;

    return 0;
}
