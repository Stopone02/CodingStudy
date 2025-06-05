N = int(input())
array = []
for i in range(N):
    a = int(input())
    array.append(a)
array = sorted(array)
for j in array:
    print(j)