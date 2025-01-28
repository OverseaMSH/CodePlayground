// https://quera.org/problemset/14580
#include <iostream>
#include <string>
using namespace std;
int main() {
    int n,x,k;
    cin>>n>>x>>k;
    string a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int i=(x-1+k)%n;
    cout<<a[i];
    return 0;
}