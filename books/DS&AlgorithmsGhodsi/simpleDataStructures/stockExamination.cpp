#include <iostream>
#include <vector>
using namespace std;

vector<int> computeSpans(vector<int> &arr)
{
    int n = arr.size();
    vector<int> s(n); 

    for (int i = 0; i < n; i++)
    {
        int span = 1; 
        int j = i - 1;

        while (j >= 0 && arr[j] <= arr[i])
        {
            span++;
            j--;
        }

        s[i] = span; 
    }

    return s;
}

int main()
{
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    vector<int> spans = computeSpans(arr);

    for (int i = 0; i < n; i++)
    {
        cout << spans[i] << " ";
    }
    cout << endl;

    return 0;
}
