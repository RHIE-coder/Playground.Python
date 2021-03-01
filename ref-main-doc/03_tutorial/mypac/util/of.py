from functools import reduce
from collections import deque

def values(*args):
    return args

def verboseOf(values, *, mapping = None, filtering = None, reducing = None):
    print("Parsing Target : ", values)
    queue = deque([mapping, filtering, reducing])
    print("Parsing Steps : ", queue)
    source = list(values)
    x = queue.popleft()
    print("Mapping Steps : ", x)
    if x != None:
        source = list(map(x,source))
        print("Mapping After: ", source)
    x = queue.popleft()
    print("Filtering Steps : ", x)
    if x != None:
        source = filter(x, source)
        print("Filtering After: ", source)
    x = queue.popleft()         
    print("Reducing Steps : ", x)
    if x != None:
        source = reduce(x, source)
        print("Reducing After: ", source)
             
    print("Result : ", source)
    
    return source

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