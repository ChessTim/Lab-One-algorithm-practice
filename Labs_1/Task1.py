import time
import random

def contains_element(arr):
    target = 10001
    for x in arr:
        if x == target:
            return True
    return False

def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    print("n\tt,с")
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(contains_element, arr)
        print(f"{n}\t{t:.6f}")
