import re

a = input().replace(' ', '')
b = re.sub(r'[^\w]', '', a)
d = b[::-1]
print(b)
print(d)
if b.lower() == d.lower():
    print("Палиндром")
else: print("Не палиндром")