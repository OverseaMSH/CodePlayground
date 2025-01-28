// https://quera.org/problemset/588
#include <iostream>

using namespace std;
int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    int max = arr[0];
    for(int j = 0; j<n;j++){
        if(arr[j]>max){
            max=arr[j];
        }
    }
    cout << max;
    return 0;
}