from callbags.sources import iterable
from callbags.transformations import map
from callbags.utilities import pipe
from callbags.sinks import iterate

pipe(
    iterable([2, 3, 5, 6]),
    map(lambda x: x * 2),
    iterate(lambda x: print(x))
)
