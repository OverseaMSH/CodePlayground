// https://quera.org/problemset/609?tab=description
#include <iostream>
#include <cmath>
using namespace std;
bool isInt(float n)
{
    return floor(n) == n;
}
const int MAX = 100;
void spiralMatrixTraversal(int matrix[MAX][MAX], int size)
{
    int top = 0, bottom = size - 1, left = 0, right = size - 1;
    int sum = 0, score = 0;

    while (top <= bottom && left <= right)
    {
        for (int i = left; i <= right; i++)
        {
            sum += matrix[top][i];
            if (isInt(sqrt(sum)) == 1)
            {
                score++;
            }
        }
        top++;

        for (int i = top; i <= bottom; i++)
        {
            sum += matrix[i][right];
            if (isInt(sqrt(sum)) == 1)
            {
                score++;
            }
        }
        right--;
        if (top <= bottom)
        {
            for (int i = right; i >= left; i--)
            {
                sum += matrix[bottom][i];
                if (isInt(sqrt(sum)) == 1)
                {
                    score++;
                }
            }
            bottom--;
        }

        if (left <= right)
        {
            for (int i = bottom; i >= top; i--)
            {
                sum += matrix[i][left];
                if (isInt(sqrt(sum)) == 1)
                {
                    score++;
                }
            }
            left++;
        }
    }
    cout << score;
}
int main()
{
    int size;
    cin >> size;
    int matrix[MAX][MAX];
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            cin >> matrix[i][j];
        }
    }
    spiralMatrixTraversal(matrix, size);
    return 0;
}
