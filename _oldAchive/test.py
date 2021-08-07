from mypac import *
from mypac.util.stream import values
stream.of(values(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
          mapping=lambda x: x * 10,
          filtering=lambda x: x % 2 == 0,
          reducing=lambda x, y: x + y)
