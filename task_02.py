#lst=input('Введите список ')
#rng=input('Введите диапазон ')

def coincidence(lst=None, rng=None):
    if lst is None or rng is None:
        return[]
    return [x for x in lst if x in rng]

print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))
    
