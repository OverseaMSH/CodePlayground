// https://quera.org/problemset/178905
#include <stdio.h>

int main() {
    int x1, y1, x2, y2, x3, y3, x4, y4;
    scanf("%d %d", &x1, &y1);
    scanf("%d %d", &x2, &y2);
    scanf("%d %d", &x3, &y3);
    scanf("%d %d", &x4, &y4);
    
    int counter = 0;

    if (x1 == x3 || y1 == y3 || x1 == x4 || y1 == y4) {
        counter++;
    }

    if (x2 == x3 || y2 == y3 || x2 == x4 || y2 == y4) {
        counter++;
    }

    if (counter == 1) {
        printf("happy\n");
    } else {
        printf("unhappy\n");
    }

    return 0;
}