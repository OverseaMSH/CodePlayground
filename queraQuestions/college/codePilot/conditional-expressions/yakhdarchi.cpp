// https://quera.org/college/4499/chapter/12637/lesson/42864
#include <iostream>
#include <string>

using namespace std;
int main()
{
    int temp;
    cin >> temp;
    if (temp > 100)
    {
        cout << "Steam";
    }
    else if (temp <0)
    {
        cout << "Ice";
    }
    else
    {
        cout << "Water";
    }
    return 0;
}
