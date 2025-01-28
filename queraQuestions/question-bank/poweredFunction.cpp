// https://quera.org/problemset/304
#include <iostream>
#include <math.h>
#include <cmath>
#include <iomanip>
using namespace std;
int main()
{
   long double Base;
   unsigned int exp;
   cin >> Base;
   cin >> exp;
    cout << fixed << setprecision(3) << pow(Base,exp);
    return 0;
}