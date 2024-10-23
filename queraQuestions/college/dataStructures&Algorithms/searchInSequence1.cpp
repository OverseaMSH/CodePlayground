// https://quera.org/college/3016/chapter/10131/lesson/60771/?comments_page=1&comments_filter=ALL
#include <iostream>
using namespace std;
int main(){
    int n,q;
    cin>>n>>q;
    int arr1[n];
    for(int i=0;i<n;i++){
        cin>>arr1[i];
    }
    int arr2[q];
    for(int i=0;i<q;i++){
        cin>>arr2[i];
    }
    for (int i=0;i<q;i++){
        int counter=0;
        for(int j=0;j<n;j++){
            if (arr2[i]>arr1[j]){
                counter++;
            }
        }
        cout<<counter<<endl;
    }
    return 0;
}