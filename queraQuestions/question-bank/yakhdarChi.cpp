// https://quera.org/problemset/3429
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
