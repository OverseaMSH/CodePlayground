from itertools import permutations

def count_inversions(perm):
    inversions = 0
    n = len(perm)
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inversions += 1
    return inversions

def count_permutations_with_k_inversions(n, k):
    count = 0
    for perm in permutations(range(1, n + 1)):
        if count_inversions(perm) == k:
            count += 1
    return count

# دریافت ورودی
n, k = map(int, input().split())
print(count_permutations_with_k_inversions(n, k))
