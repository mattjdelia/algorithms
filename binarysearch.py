'''
Implementation of a binary search function in Python 2.7
Designed to be somewhat unbreakable, though there may still be bugs somewhere
'''

def get_range():
    while True:
        try:
            ran = int(raw_input("Enter a range:"))
            while True:
                try:
                    x = range(ran)
                    return x
                except MemoryError:
                    print "That array is toooooooooo big."
                    ran = int(raw_input("Enter a range:"))
                    continue
                except OverflowError:
                    print "That number is toooooooooo big."
                    ran = int(raw_input("Enter a range:"))
                    continue
        except ValueError:
            print "List range requires an integer value."
        else:
            return ran
            break

def validate_num():
    while True:
        try:
            y = int(raw_input("Enter number to search:"))
            if isinstance(y, int):
                return y
        except ValueError:
            print "Those characters or numbers are invalid. Try an integer."
        else:
            return y
            break

r = get_range()
n = validate_num()

def binary_search(numset,x):
    low = 0
    high = len(numset) - 1
    while True:
        if low > high:break
        mid = (low + high)/2
        if numset[mid] < x:
            low = mid + 1
        elif numset[mid] > x:
            high = mid - 1
        elif numset[mid] == x:
            return mid



print binary_search(r,n)
