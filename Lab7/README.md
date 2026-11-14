# Lab 7 - Algorithm Complexity Analysis

This lab contains 22 Python code snippets. Each snippet is analysed for time and space complexity using Big-O notation.

---

## Snippet 1 — `find_max`

```python
def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val
```

| | Complexity |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

**Justify:** The loop checks every element once and uses only one extra variable.

---

## Snippet 2 — `has_duplicate`

```python
def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```

| | Complexity |
|---|---|
| **Time** | O(n²) |
| **Space** | O(1) |

**Justify:** Nested loops compare every pair of elements. No extra list is created.

---

## Snippet 3 — `sum_digits`

```python
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
```

| | Complexity |
|---|---|
| **Time** | O(d) |
| **Space** | O(d) |

**Justify:** The function processes each digit using recursion. Here, d is the number of digits.

---

## Snippet 4 — `print_pairs`

```python
def print_pairs(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(n):
            result.append((arr[i], arr[j]))
    return result
```

| | Complexity |
|---|---|
| **Time** | O(n²) |
| **Space** | O(n²) |

**Justify:** Two nested loops create n² pairs, which are stored in a list.

---

## Snippet 5 — `binary_search`

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

| | Complexity |
|---|---|
| **Time** | O(log n) |
| **Space** | O(1) |

**Justify:** The search area becomes half in every step. Only a few variables are used.

---

## Snippet 6 — `matrix_multiply`

```python
def matrix_multiply(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result
```

| | Complexity |
|---|---|
| **Time** | O(n³) |
| **Space** | O(n²) |

**Justify:** Three nested loops perform n³ operations. The result matrix stores n² elements.

---

## Snippet 7 — `to_sparse`

```python
def to_sparse(matrix):
    triples = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != 0:
                triples.append((r, c, matrix[r][c]))
    return triples
```

| | Complexity |
|---|---|
| **Time** | O(m × n) |
| **Space** | O(k) |

**Justify:** Every matrix element is checked once. Only k non-zero elements are stored.

---

## Snippet 8 — `process`

```python
def process(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i])
    for j in range(n):
        for k in range(n):
            print(arr[j], arr[k])
```

| | Complexity |
|---|---|
| **Time** | O(n²) |
| **Space** | — |

**Justify:** The first loop takes O(n), while the nested loops take O(n²). The larger complexity is O(n²).

---

## Snippet 9 — `check_first_ten`

```python
def check_first_ten(arr):
    for i in range(len(arr)):
        for j in range(10):
            if arr[i] == j:
                return True
    return False
```

| | Complexity |
|---|---|
| **Time** | O(n) |
| **Space** | — |

**Justify:** The inner loop runs only 10 times, which is constant. Therefore, the overall complexity is O(n).

---

## Snippet 10 — `reverse_new`

```python
def reverse_new(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
```

| | Complexity |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

**Justify:** Every element is copied once into a new list of size n.

---

## Snippet 11 — `reverse_in_place`

```python
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

| | Complexity |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

**Justify:** Elements are swapped in the same list. No extra list is created.

---

## Snippet 12 — `factorial`

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

| | Complexity |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

**Justify:** The function makes n recursive calls, and each call uses stack memory.

---

## Snippet 13 — `fibonacci`

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

| | Complexity |
|---|---|
| **Time** | O(2ⁿ) |
| **Space** | O(n) |

**Justify:** Each call creates two more calls. The maximum recursion depth is n.

---

## Snippet 14 — `count_pairs_with_sum`

```python
def count_pairs_with_sum(arr, target):
    seen = set()
    count = 0
    for num in arr:
        if target - num in seen:
            count += 1
        seen.add(num)
    return count
```

| | Complexity |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

**Justify:** Each element is checked once using a set. The set can store up to n elements.

---

## Snippet 15 — `print_all_subsets`

```python
def print_all_subsets(arr):
    n = len(arr)
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        print(subset)
```

| | Complexity |
|---|---|
| **Time** | O(n × 2ⁿ) |
| **Space** | — |

**Justify:** There are 2ⁿ possible subsets, and each subset checks n elements.

---

## Snippet 16 — `merge_sorted`

```python
def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
```

Let m = length of a and n = length of b.

| | Complexity |
|---|---|
| **Time** | O(m + n) |
| **Space** | O(m + n) |

**Justify:** Every element from both lists is added once to the result list.

---

## Snippet 17 — `is_palindrome`

```python
def is_palindrome(s):
    return s == s[::-1]
```

| | Complexity |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

**Justify:** Reversing the string creates a new copy and takes O(n) time and space.

---

## Snippet 18 — `flatten`

```python
def flatten(matrix):
    flat = []
    for row in matrix:
        for val in row:
            flat.append(val)
    return flat
```

Let the matrix have m rows and n columns.

| | Complexity |
|---|---|
| **Time** | O(m × n) |
| **Space** | O(m × n) |

**Justify:** Every matrix element is visited once and stored in a new list.

---

## Snippet 19 — `power`

```python
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
```

| | Complexity |
|---|---|
| **Time** | O(exp) |
| **Space** | O(exp) |

**Justify:** The exponent decreases by one in every recursive call. Each call uses stack memory.

---

## Snippet 20 — `fast_power`

```python
def fast_power(base, exp):
    if exp == 0:
        return 1
    half = fast_power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return half * half * base
```

| | Complexity |
|---|---|
| **Time** | O(log exp) |
| **Space** | O(log exp) |

**Justify:** The exponent is divided by two in every call, reducing the number of recursive calls.

---

## Snippet 21 — `has_common_element`

```python
def has_common_element(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True
    return False
```

Let p = length of a and q = length of b.

| | Complexity |
|---|---|
| **Time** | O(p × q) |
| **Space** | O(1) |

**Justify:** Every element of one list may be compared with every element of the other list.

---

## Snippet 22 — `build_frequency_map`

```python
def build_frequency_map(arr):
    freq = {}
    for val in arr:
        freq[val] = freq.get(val, 0) + 1
    return freq
```

| | Complexity |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

**Justify:** Every element is processed once. The dictionary can store up to n unique elements.


## Reference Table

| # | Function | Time | Space |
|---|---|---|---|
| 1 | `find_max` | O(n) | O(1) |
| 2 | `has_duplicate` | O(n²) | O(1) |
| 3 | `sum_digits` | O(d) | O(d) |
| 4 | `print_pairs` | O(n²) | O(n²) |
| 5 | `binary_search` | O(log n) | O(1) |
| 6 | `matrix_multiply` | O(n³) | O(n²) |
| 7 | `to_sparse` | O(m × n) | O(k) |
| 8 | `process` | O(n²) | — |
| 9 | `check_first_ten` | O(n) | — |
| 10 | `reverse_new` | O(n) | O(n) |
| 11 | `reverse_in_place` | O(n) | O(1) |
| 12 | `factorial` | O(n) | O(n) |
| 13 | `fibonacci` | O(2ⁿ) | O(n) |
| 14 | `count_pairs_with_sum` | O(n) | O(n) |
| 15 | `print_all_subsets` | O(n × 2ⁿ) | — |
| 16 | `merge_sorted` | O(m + n) | O(m + n) |
| 17 | `is_palindrome` | O(n) | O(n) |
| 18 | `flatten` | O(m × n) | O(m × n) |
| 19 | `power` | O(exp) | O(exp) |
| 20 | `fast_power` | O(log exp) | O(log exp) |
| 21 | `has_common_element` | O(p × q) | O(1) |
| 22 | `build_frequency_map` | O(n) | O(n) |
