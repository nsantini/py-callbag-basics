def map(f):
    def setSource(source):
        def callbag(start, sink):
            if (start != 0):
                return
            def cb(t, d):
                nonlocal sink
                sink(t, f(d) if t == 1 else d)
            source(0, cb)
        return callbag
    return setSource