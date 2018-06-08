def pipe(*argvs):
    cbs = [cb for cb in argvs]
    res = cbs[0]
    n = len(cbs)
    for i in range(1, n):
        res = cbs[i](res)
    return res