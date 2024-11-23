//https://quera.org/problemset/616
#include <iostream>
using namespace std;
int main() {
    int n;cin>>n;
    int base=1;
    while(base<n){
        base*=2;
    }
    cout<<base;
    return 0;
}