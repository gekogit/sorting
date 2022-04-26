def max_heapify(input, n, i):
    l = left(i)
    r = right(i)
    if l < n and input[l] < input[i]:
        largest = l
    else:
        largest = i
    if r < n and input[r] < input[largest]:
        largest = r
    if largest != i:
        input[i], input[largest] = input[largest], input[i]
        max_heapify(input, n, largest)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def heap_sort(input):
    n = len(input)
    for i in range(n, -1, -1):
        max_heapify(input, n, i)
    for i in range(n-1, 0, -1):
        input[0], input[i] = input[i], input[0]
        max_heapify(input, i, 0)


if __name__ =='__main__':
    input = [33, 35, 42, 10, 7, 8, 14, 19, 48]
    heap_sort(input)
    print(input)