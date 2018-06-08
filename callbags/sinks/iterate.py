def iterate(operation):
    def setSource(source):
        talkback = None
        def sink(t, d):
            nonlocal talkback
            if (t == 0):
                talkback = d
            if (t == 1):
                operation(d)
            if (t == 1 or t == 0) and talkback:
                talkback(1)
        source(0, sink)
    return setSource