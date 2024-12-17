# https://quera.org/college/3016/chapter/8236/lesson/60803/
n, k = map(int, input().split())
elems = list(map(int, input().split()))

if k ==1 :
    print(max(elems))
elif k ==2:
    print(min([elems[0],elems[-1]]))
elif k >=3:
    print(min(elems))
