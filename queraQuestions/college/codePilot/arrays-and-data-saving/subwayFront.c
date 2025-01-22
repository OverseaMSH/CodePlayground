// https://quera.org/college/4499/chapter/12639/lesson/256136/
#include <stdio.h>

int main()
{
    int a[8], b[8];
    for (int i = 0; i < 8; i++)
    {
        scanf("%d", &a[i]);
    }
    for (int i = 0; i < 8; i++)
    {
        scanf("%d", &b[i]);
    }
    int counter=0;
    for (int i = 0; i < 8; i++){
        if (a[i]==1 && b[i]==1){
            counter++;
        }
    }
    printf("%d", counter);
    return 0;
}