'''
Given a list of integers, write a function that determines whether the list consists of a "single complete cycle"
A list X consists of a "single complete cycle" if and only if, given
    X is a set (list) containing some number of integers x indexed by a set I (as all Python lists are), and
    N is a set of iterators n (consecutive integers; though also implied in Python),
    the following function is a bijection from N to X (the set of iterators N is to return each integer in X once and only once)
    If n = 1: i = 0, f(n) = x.i
    If 1 < n <= len(X): i = f(n - 1), f(n) = x.i
 
 E.g., given a set [1, 5, 2], 
     n = 1: i = 0, f(n) = 1
     n = 2: i = f(n - 1), f(n) = 5
     n = 3: i = f(n - 1), f(n) = 2
 
'''


print("Enter list elements by putting spaces between each integer.")

X = [int(a) for a in input().split()]

if len(X) <= 1:
    print("COMPLETE")
    quit()

n = 0
index = 0
count = 0
index_bank = []

while True:
    if count >= len(X):
        print("COMPLETE")
        break
    else:
        if index in index_bank:
            print("INCOMPLETE")
            break
        else:
            index_bank.append(index)
    n = X[index]
    print(n)
    index = n % len(X)
    count += 1
