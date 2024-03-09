def f(n):
    s1 = int(str(n)[0]) + int(str(n)[1])
    s2 = int(str(n)[1]) + int(str(n)[2])
    return str(s1)+str(s2)

for i in range(100, 1000):
    if f(i) == '159':
        print(i)
        break
