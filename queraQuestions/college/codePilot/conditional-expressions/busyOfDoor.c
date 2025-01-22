// https://quera.org/college/4499/chapter/12637/lesson/42862
#include <stdio.h>
int main() {
    int hw,hh,mw,mh;
    scanf("%d %d",&hw,&hh);
    scanf("%d %d",&mw,&mh);
    if(hw>=mw && hh>=mh){
        printf("yes");
    }else{
        printf("no");
    }

    return 0;
}