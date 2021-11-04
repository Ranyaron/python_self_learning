N = 1000
a = [True] * N
a[0] = a[1] = False
lis = []

for k in range(2, N):
    if a[k]:
        for m in range(2 * k, N, k):
            a[m] = False
        lis.append(k)

# for k in range(N):
#     print(k, '-', 'простое' if a[k] else 'составное')

print(lis)
