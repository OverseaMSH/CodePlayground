// https://quera.org/college/4499/chapter/12636/lesson/43176
#include <stdio.h>
int main()
{
    int a, d, n;
    scanf("%d %d %d", &a, &d, &n);
    int sum = (a * 2 + ((n - 1) * d)) * n / 2;
    printf("%d", sum);
    return 0;
}