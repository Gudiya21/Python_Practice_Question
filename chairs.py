t = int(input("enter t"))
ans = []

for i in range(t):
    n = int(input("enter n"))
    s = input()
    s2 = 2 * s 
    k = 0
    m = 0
    while k < n:
        if s2[k] == '0':
            e = k
            while e < 2 * n and s2[e] == '0':
                e += 1
            l = e - k
            if l > m:
                m = l
            k = e
        else:
            k += 1
    c = 0
    for j in range(n):
        if s[j] == '0':
            c += 1
    ans.append(c - m)
print(*ans)

# 4
# 20 14
# 41 41
# 35 0
# 50 100