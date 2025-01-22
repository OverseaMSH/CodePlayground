// https://quera.org/problemset/276?tab=description
#include <stdio.h>

int main() {
    int m, s;
    scanf("%d %d", &m, &s);

    if (s == 0 && m == 1) {
        printf("0 0\n");
        return 0;
    }
    if (s == 0 || s > 9 * m) {
        printf("-1 -1\n");
        return 0;
    }

    int smallest[m];
    int remaining_sum = s;

    for (int i = m - 1; i >= 0; i--) {
        if (remaining_sum > 9) {
            smallest[i] = 9;
            remaining_sum -= 9;
        } else {
            smallest[i] = remaining_sum;
            remaining_sum = 0;
        }
    }

    if (smallest[0] == 0) {
        for (int i = 1; i < m; i++) {
            if (smallest[i] > 0) {
                smallest[i]--;
                smallest[0] = 1;
                break;
            }
        }
    }

    for (int i = 0; i < m; i++) {
        printf("%d", smallest[i]);
    }
    printf(" ");

    int largest[m];
    remaining_sum = s;
    for (int i = 0; i < m; i++) {
        if (remaining_sum >= 9) {
            largest[i] = 9;
            remaining_sum -= 9;
        } else {
            largest[i] = remaining_sum;
            remaining_sum = 0;
        }
    }

    for (int i = 0; i < m; i++) {
        printf("%d", largest[i]);
    }
    printf("\n");

    return 0;
}
