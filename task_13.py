from collections import OrderedDict
import time
from functools import wraps

def cached(max_size=None, seconds=None):
    if not isinstance(max_size, (int, type(None))): #проверка на целочисленность
        max_size=None
    if not isinstance(seconds, (int, type(None))):
        seconds = None

    def decorator(func):
        cache = OrderedDict() #форм кэш

        @wraps(func)
        def wrapper(*args, **kwargs):#ключ кэша
            cache_key = (args, frozenset(kwargs.items()))

            if cache_key in cache:
                result, timestamp = cache[cache_key]
                if seconds is None or (time.time() - timestamp) < seconds:
                    return result
                del cache[cache_key]

            result = func(*args, **kwargs)
            
            cache[cache_key] = (result, time.time())

            if max_size is not None and len(cache) > max_size:
                cache.popitem(last=False)

            return result

        return wrapper
    return decorator

@cached(max_size=3, seconds=10)
def slow_function(x):
    print(f"Вычисляю для {x}...")
    return x ** 2 


print(slow_function(2))
print(slow_function(2)) 
time.sleep(15)
print(slow_function(2)) 