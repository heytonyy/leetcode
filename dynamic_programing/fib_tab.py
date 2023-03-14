# practice from: https://youtu.be/oBt53YbR9Kk

def fib_tab(n):  
    # trivial case
    if n == 0:
        return 0
    # make table with n+1 elements (bc zero-index)
    table = [ 0 for _ in range(n+1) ]
    # adjust given values (for fib: f0=0, f1=0)
    table[1] = 1 
    # stop 2 before end, can go out of range
    for i in range(n-1):
        table[i+1] += table[i]
        table[i+2] += table[i]
    # adjust for last element bc stopped 2 early
    table[i+2] += table[i+1]

    return table[n]


# TESTING
print(fib_tab(0)) # 0
print(fib_tab(4)) # 3
print(fib_tab(6)) # 8
print(fib_tab(9)) # 34
print(fib_tab(100)) # 354224848179261915075

