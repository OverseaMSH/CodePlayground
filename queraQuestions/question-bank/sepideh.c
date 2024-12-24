// https://quera.org/problemset/31020
#include <stdio.h>
int main() {
    int n,m;
    scanf("%d %d",&n,&m);
    if(n%m==0){
        printf("%d",n/m);
    }else{
        printf("%d",((int)n/m)+1);
    }
    return 0;
}