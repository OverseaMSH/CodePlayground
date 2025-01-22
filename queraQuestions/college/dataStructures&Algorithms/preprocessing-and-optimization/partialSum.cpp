#include <iostream>
using namespace std;
int main()
{
    int n, q;
    cin >> n >> q;
    int arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    int queries[q][2];
    for (int i = 0; i < q; i++)
        cin >> queries[i][0] >> queries[i][1];
    int partialSum[n + 1];
    partialSum[0] = 0;
    for (int i = 1; i <= n; i++)
        partialSum[i] = partialSum[i - 1] + arr[i - 1];

    for (int i = 0; i < q; i++)
    {
        int l = queries[i][0];
        int r = queries[i][1];
        cout << partialSum[r + 1] - partialSum[l] << endl;
    }
}
