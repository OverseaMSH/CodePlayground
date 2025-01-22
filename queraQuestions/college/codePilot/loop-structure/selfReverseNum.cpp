// https://quera.org/college/4499/chapter/12638/lesson/42873/
#include <iostream>
#include <math.h>
#include <cmath>
#include <iomanip>
using namespace std;
int main()
{
    int n, reversed;

    reversed = 0;
    cin >> n;
    const int number = n;

    while (n > 0)
    {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    if(number==reversed){
        cout << "YES";
    }else{
        cout << "NO";
    }
    return 0;
}