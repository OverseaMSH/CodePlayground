// https://quera.org/college/4499/chapter/12636/lesson/42859
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