// https://quera.org/problemset/51865
#include <iostream>
using namespace std;
int main()
{
    double grade, days;
    cin >> grade;
    cin >> days;
    if (days == 0)
    {
        cout << 20;
    }
    else if (days == 7)
    {
        cout << grade;
    }
    else
    {
        if (grade - days < 0)
        {
            cout << 0;
        }
        else
        {
            cout << grade - days;
        }
    }
    return 0;
}
