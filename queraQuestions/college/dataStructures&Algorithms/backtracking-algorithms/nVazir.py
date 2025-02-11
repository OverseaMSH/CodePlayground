def kQueen(n, k, col, rows, diag1, diag2):
    if col == n:
        return 1 if k == 0 else 0

    ways = 0
    if k > 0:
        for i in range(n):
            if i in rows or (col + i) in diag1 or (col - i) in diag2:
                continue  
            
            rows.add(i)
            diag1.add(col + i)
            diag2.add(col - i)

            ways += kQueen(n, k - 1, col + 1, rows, diag1, diag2)

            rows.remove(i)
            diag1.remove(col + i)
            diag2.remove(col - i)

    ways += kQueen(n, k, col + 1, rows, diag1, diag2)  
    return ways

n, k = map(int, input().split())
print(kQueen(n, k, 0, set(), set(), set()))
