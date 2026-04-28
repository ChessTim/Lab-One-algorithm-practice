1. Реализация
```python
def Value_in_arr(arr, search_value):
    for x in arr:
        if x == search_value:
            return True
    return False
```

2. Функция измерения времени
```python
from time import *


def measure_time(func, *data):
    start = perf_counter()
    func(*data)
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

4. Эксперимент
```python
from time import *
from random import*


def Value_in_arr(arr, search_value):
    for x in arr:
        if x == search_value:
            return True
    return False


def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(randint(0, 10_000))
    return arr


def measure_time(func, *data):
    start = perf_counter()
    func(*data)
    end = perf_counter()
    return end - start


if __name__ == "__main__":
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(Value_in_arr, arr, randint(0, 10_000))
        print(n, t)
```
|         n          |            t           |
|--------------------|------------------------|
| 100                | 3.3000251            |
| 1000               | 2.8999987            |
| 5000               | 0.0001241            |
| 10000              | 0.0002376              |