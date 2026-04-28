1. Реализация
```python
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

2. Функция измерения времени
```python
from time import *

def measure_time(func, data):
    start = perf_counter()
    func(data)
    end = perf_counter()
    return end - start
```

3. Функция генерации данных
```python
from random import *

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(randint(0, 10_000))
    return arr
```

4. Функция измерения памяти
```python
from tracemalloc import *

def measure_memory(func, data):
    start()
    func(data)
    current, peak = get_traced_memory()
    stop()
    return peak / 1024
```


5. Эксперимнт
```python
from time import *
from random import *
from tracemalloc import *

def measure_time(func, data):
    start = perf_counter()
    func(data)
    end = perf_counter()
    return end - start

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(randint(0, 10_000))
    return arr

def measure_memory(func, data):
    start()
    func(data)
    current, peak = get_traced_memory()
    stop()
    return peak / 1024

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(bubble_sort, arr)
        m = measure_memory(bubble_sort, arr)
        print(n, t, m)
```
| n      | t       | m      |
|--------|---------|--------|
| 100    | 0.001240 | 0.0   |
| 1000   | 0.313896 | 0.0   |
| 5000   | 6.016538 | 0.0   |
| 10000  | 22.431478 | 0.0   |