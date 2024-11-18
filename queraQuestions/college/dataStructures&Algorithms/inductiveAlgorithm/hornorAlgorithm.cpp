#include <iostream>
#include <cmath>

using namespace std;
int main() {
    int n,x;
    cin>>n>>x;
    int arr[n+1];
    for(int i=0;i<n+1;i++){
        cin>>arr[i];
    }
    int sum=0;
    for (int i=n;i>=0;i--){
        sum+=pow(x,i)*arr[n-i];
    }
    cout<<sum;
    return 0;
}