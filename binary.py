import random
import time

# naive_search
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search
def binary_search(l, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (high + low) // 2
    
    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] > target:
        return binary_search(l, target, low, midpoint - 1)
    else:
        # l[midpoint] < target:
        return binary_search(l, target, midpoint + 1, high)

# compare the time result
length = 10000 # list of "length" number

num_list = set()

while len(num_list) < length:
    num_list.add(random.randint(-20000, 20000))
num_list = sorted(list(num_list))

start = time.time()
for target in num_list:
    naive_search(num_list, target)
end = time.time()
search_time = "{:.2f}".format(end - start)
print(f"Naive time: {search_time} seconds")

start = time.time()
for target in num_list:
    binary_search(num_list, target)
end = time.time()
search_time = "{:.2f}".format(end - start)
print(f"Binary time: {search_time} seconds")