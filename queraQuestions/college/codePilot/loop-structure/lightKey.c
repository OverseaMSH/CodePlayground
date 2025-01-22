// https://quera.org/college/4499/chapter/12638/lesson/256164
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int x; 
    int counter = 0; 

    scanf("%d", &x);
    for (int i = 1; i < n; i++) {
        int a;
        scanf("%d", &a); 
        if (a != x) { 
            counter++; 
            x = a;
        }
    }

    printf("%d\n", counter);
    return 0;
}