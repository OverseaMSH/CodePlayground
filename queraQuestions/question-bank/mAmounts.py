# https://quera.org/problemset/76278
def calculator(n, m, ls):
    newArr = []
    arr = []
    for i in range(0, n, m):
        arr.append(ls[i:i + m])
    for one in arr:
        newArr.append(sum(one))
    summary = 0
    for i in range(len(newArr)):
        if i % 2 == 0:
            summary += newArr[i]
        else:
            summary -= newArr[i]
    return summary

