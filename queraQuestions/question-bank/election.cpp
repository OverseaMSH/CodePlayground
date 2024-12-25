// https://quera.org/problemset/604
#include <iostream>
using namespace std;
int president(int candidateNumber)
{
    if (candidateNumber == 1)
    {
        return 1;
    }
    else
    {
        return ((president(candidateNumber - 1) + 1) % candidateNumber) + 1;
    }
}
int main()
{
    int candidateNumber;
    cin >> candidateNumber;
    cout << president(candidateNumber);
}