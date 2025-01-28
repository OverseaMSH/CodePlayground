// https://quera.org/problemset/177663
#include <iostream>
using namespace std;
int main(){
    int n,a,b,c,d;
    cin>>n>>a>>b>>c>>d;
    int counter=0;
    for (int i=1;i<=n;i++){
        if (i%a==0 || i%b==0 || i%c==0 || i%d==0){
            counter++;
        }
    }
    cout<<counter;
    return 0;
} 