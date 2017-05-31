def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib2(n):
    a, b = 1, 2
    for i in range(n):
        a, b = b, a + b
    return a


def fib3(n):
    if n == 1:
        return 1
    else:
        return n * fib3(n - 1)


def power(n):
    if n == 1:
        return 2
    else:
        return 2 * power(n - 1)

# Sort testing algorithm


def is_sorted(x):
    n = len(x)
    sorted = True
    for i in range(n - 1):
        if x[i] > x[i + 1]:
            sorted = False
    return sorted

# Bubble sort


def bubble_sort(x):
    n = len(x)
    for j in range(n):  # n-1이어도 될 듯
        for i in range(n - 1):
            if x[i] > x[i + 1]:
                (x[i + 1], x[i]) = (x[i], x[i + 1])


def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        while i >= 0 and a[i - 1] > key:
            a[i] = a[i - 1]
            i -= 1
        a[i] = key

k = 0


def f(n):
    global k
    if n == 0:
        k = k + 1
        return 1
    else:
        return f(n - 1) + f(n - 1)


def g(n):
    k = 0
    i = n
    while i > 1:
        k = k + 1
        i = i / 2
    return k

# queue


class queue():

    def __init__(self, n):
        self.items = [i for i in range(n)]
        self.head = 0
        self.tail = 0
        self.length = self.tail - self.head

    def put(self, x):
        self.items.append(x)

    def get(self):
        leftpop = self.items[0]
        del self.items[0]
        return leftpop

    def getitem(self):
        return self.items[self.head:self.tail]

    def enque(self, x):
        try:
            self.items[self.tail] = x
            self.tail += 1
        except:
            print("full")

    def deque(self):
        try:
            x = self.items[self.head]
            self.head += 1
            return x
        except:
            print("empty")


# # stack

class stk():

    def __init__(self, n):
        self.items = [i for i in range(n)]
        self.top = -1
        self.max = n

    def getitem(self):
        return self.items[:self.top + 1]

    def stack_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, x):
        if self.top < self.max - 1:
            self.items[self.top + 1] = x
            self.top += 1
        else:
            print("full")

    def pop(self):
        if self.stack_empty() == True:
            print("empty")
        else:
            self.top -= 1
            return self.items[self.top + 1]


# # Binary search


def binary_search(A, L, R, a):
    if L < R:
        m = int((R + L) / 2)
        if a < A[m]:
            return binary_search(A, L, m - 1, a)
        elif a > A[m]:
            return binary_search(A, m + 1, R, a)
        else:
            return m
    else:
        return -1

# # Merge sort


def merge(A, p, r):
    m = (p - r) // 2
    ls = A[p:m]
    rs = A[m:r]
    ls.append(float('inf'))
    rs.append(float('inf'))
    L = 0
    R = 0
    for i in range(p, r):
        if ls[L] < rs[R]:
            A[i] = ls[L]
            L += 1
        else:
            A[i] = rs[R]
            R += 1


def merge_sort(A, p, r):
    if p + 1 < r:
        m = (p + r) // 2
        merge_sort(A, p, m)
        merge_sort(A, m, r)
        merge(A, p, r)

# # Heap


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(A, i, n):
    l = left(i)
    r = right(i)
    if l < n and A[i] < A[l]:
        largest = l
    else:
        largest = i
    if r < n and A[largest] < A[r]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, n)


def build_heap(A):
    for i in range(int(len(A) / 2), 0, -1):
        max_heapify(A, i - 1, len(A))


def heap_sort(A):
    build_heap(A)
    for i in range(len(A), 1, -1):
        A[i - 1], A[0] = A[0], A[i - 1]
        max_heapify(A, 0, i - 1)

# Quick sort


def partition(A, p, r):

    x = A[r - 1]
    i = p - 1
    for j in range(p, r - 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r - 1] = A[r - 1], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q)
        quick_sort(A, q + 1, r)
