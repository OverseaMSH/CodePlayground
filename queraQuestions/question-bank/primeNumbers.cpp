// https://quera.org/problemset/293
#include <iostream>

using namespace std;
int main()
{
    int n, m;
    cin >> n;
    cin >> m;
    for (n; m >= n; n++)
    {
        int counter = 0;

        for (int i = 1; i <= n; i++)
        {
            if (n % i == 0)
            {
                counter++;
            }
        }
        if (counter == 2)
        {
            cout << n<<endl;
        }
    }

    return 0;
}