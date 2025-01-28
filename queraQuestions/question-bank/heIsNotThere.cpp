// https://quera.org/problemset/3538
#include <iostream>
#include <set>
#include <string>
using namespace std;
int main() {
    int a;
    cin>>a;
    string aS[a];
    set<string> days;
    for(int i=0;i<a;i++){
        cin>>aS[i];
        days.insert(aS[i]);
    }
        int b;
    cin>>b;
    string bS[b];
    for(int i=0;i<b;i++){
        cin>>bS[i];
        days.insert(bS[i]);
    }
    int c;
    cin>>c;
    string cS[c];
    for(int i=0;i<c;i++){
        cin>>cS[i];
        days.insert(cS[i]);
    }
    cout<<7-days.size();
}
