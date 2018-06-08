def iterable(source):
    def callbag(start, sink):
        if (start != 0):
            return
        for i in source:
            sink(1, i)
    return callbag