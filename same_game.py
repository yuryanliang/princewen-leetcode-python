for n in range(2, 10):
    for x in range(2, n):
        if n % x ==0:
            break
    else:
        print(n)
try:
    s
except:
    IOError