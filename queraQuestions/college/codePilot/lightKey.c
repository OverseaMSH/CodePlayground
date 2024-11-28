// https://quera.org/college/4499/chapter/12638/lesson/256164
#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int x;
    int counter=0;
    for(int i=0;i<n;i++){
        int a;
        scanf("%d", &a);
        if(i>0){
            if(a!=x){
                x=a;
                counter++;

            }else{
                x=a;
            }
        }
    }
    printf("%d", counter);
    return 0;
}