// https://quera.org/college/4499/chapter/12637/lesson/42866
#include <iostream>
using namespace std;
int main() {
    float a,b,c;
    cin>>a>>b>>c;
    float mean=(a+b+c)/3;
    if (a==mean && b==mean && c==mean){
        cout<<0;
    }else if(a!=mean && b!=mean && c!=mean){
        cout<<2;
    }else{
        cout<<1;
    }
    return 0;
}