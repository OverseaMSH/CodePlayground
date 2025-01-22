#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int counter = 0;
    while (n >= 10)
    {
        n -= 10;
        counter++;
    }
    while (n >= 5)
    {
        n -= 5;
        counter++;
    }
    while (n >= 1)
    {
        n -= 1;
        counter++;
    }
    cout<<counter;
}