def backtrack(r, n, sequences, mark):
    if r == n:  
        return 1
    
    result = 0
    for x in sequences[r]:
        if not mark[x]:  
            mark[x] = True
            result += backtrack(r + 1, n, sequences, mark)
            mark[x] = False  
    
    return result

n = int(input())
sequences = []
for _ in range(n):
    line = list(map(int, input().split()))
    sequences.append(line[1:]) 

mark = [False] * 1000001  

result = backtrack(0, n, sequences, mark)
print(result)
