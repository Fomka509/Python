a = list(range(10000001))
a[1] = 0
lst = []
k = 2
for k in range(10000001):
    if a[k] != 0:
        lst.append(a[k])
        for p in range(k, 10000001, k):
            a[p] = 0
    k += 1
f = open('simple_number.txt', 'w')
f.write(str(lst))
f.close
