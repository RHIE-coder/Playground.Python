from functools import reduce
from collections import deque

def values(*args):
    return args

def of(values, *, mapping = None, filtering = None, reducing = None):
    queue = deque([mapping, filtering, reducing])
    source = list(values)
    x = queue.popleft()
    if x != None:
        source = list(map(x,source))
    x = queue.popleft()
    if x != None:
        source = filter(x, source)
    x = queue.popleft()            
    if x != None:
        source = reduce(x, source)
                
    return source