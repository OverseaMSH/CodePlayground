#include <stdio.h>
int main() {
    int n;
    scanf("%d",&n);
    int counter=0;
    for (int i=1;i<n;i++){
        for(int j=i;j<n-i;j++){
            int k=n-i-j;
            if (i+j>k && k>=j){
                counter++;
            }
        }
    }
    printf("%d",counter);
    return 0;
}