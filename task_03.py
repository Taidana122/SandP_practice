def max_odd(array):
    max_odd1 = None
    for item in array:
        if isinstance(item, (int, float)):
            if item == int(item):
                if int(item) % 2 != 0:
                    if max_odd1 is None or int(item) > max_odd1:
                        max_odd1 = int(item)
    
    return max_odd1
print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))