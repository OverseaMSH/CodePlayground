// https://quera.org/college/3016/chapter/8236/lesson/167525
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int n, r;
    cin >> n >> r;
    int arr[n];
    for (int i; i < n; i++)
    {
        cin >> arr[i];
    }
    sort(arr, arr + n);
    int sum=0;
    for(int i=0;i<n;i++){
        
        sum+=arr[i];
        if(sum>=r){
            cout<<i;
            break;
        }else{
            if (i==n-1){
                cout<<i+1;
            }
        }
        
    }
    
}
