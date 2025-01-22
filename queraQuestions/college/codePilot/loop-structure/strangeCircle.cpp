// https://quera.org/college/4499/chapter/12638/lesson/42876
#include <iostream>
using namespace std;
int main() {
    int n,k;
    cin>>n>>k;
    int i=1;
    int counter=0;
    while(true){
        i+=k;
        counter++;
        if (i%n==1){
            break;
        }
    }
    cout<<counter;
    return 0;
}