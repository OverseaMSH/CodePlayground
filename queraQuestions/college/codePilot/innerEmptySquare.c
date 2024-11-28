#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    
    if (b >= a) {
        printf("%s\n", "Wrong order!");
    } else {
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < a; j++) {
                if (j < b && i<b || j > b - a+1 && i>b-a+1) {
                    printf("%c", '*');  
                } else {
                    printf("%c", ' '); 
                }
            }
            printf("\n");
        }
    }
    
    return 0; 
}