#include <iostream>
using namespace std;
int main() {
    long long max= -99999999;
    int n;
    cin>>n;
    int arr[n];
    for (int i=0;i<n;i++){
        cin>>arr[i];
    }
    
    for (int i=0;i<n;i++){
        int sum=0;
        for(int j=0;j<n-i;j++){
            sum+=arr[i+j];
            if(sum>max){
                max=sum;
            }
        }
    }
    cout<<max;
    return 0;
}