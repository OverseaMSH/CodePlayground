// https://quera.org/college/4499/chapter/12638/lesson/42877
#include <iostream>
using namespace std;
int main() {
    int n;
    int a[100],b[100];
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
        for(int i=0;i<n;i++){
        cin>>b[i];
    }
    int s=0;
    for(int i=0;i<n;i++){
        s+=a[i]*b[i];
    }
    cout<<s;
    return 0;
}