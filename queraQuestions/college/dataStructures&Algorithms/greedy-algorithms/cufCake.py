# https://quera.org/college/3016/chapter/8236/lesson/60803/
import math
n, k = map(int, input().split())
arr = list(map(int, input().split()))
k=math.floor(int(n/k))+1
subarrays = [arr[i:i + k] for i in range(0, n, k)]
finalArr=[]
for i in  subarrays:
    finalArr.append(max(i))
print(min(finalArr))
