def demo(a, b):
    print('Before: ', id(a), id(b))
    a = [1, 2]
    b = [1, 2]
    print('After:', id(a), id(b))


demo([1, 2], [1, 2])
