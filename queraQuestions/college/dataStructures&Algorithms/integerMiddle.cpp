#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    int mid;
    if (n%2==0){
        mid=arr[(n/2)-1];
    }else{
        mid=arr[n/2];
    }
    int op=0;
    for(int i=0;i<n;i++){
        op+=abs(arr[i]-mid);
    }
    cout<<mid<<" "<<op;
}