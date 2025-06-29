import math
def multiply_numbers(inputs=None):
    if inputs is None:
        return None
    stroka=str(inputs)
    return[math.prod(int(x) for x in stroka if x.isdigit())]

print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))