// https://quera.org/college/4499/chapter/12637/lesson/256161
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