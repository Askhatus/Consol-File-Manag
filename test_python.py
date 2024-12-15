# функция filter
ages = [15, 28, 46, 13, 42, 14, 37, 52, 10, 9, 68]
#adult = filter(lambda x: x > 18, ages)
#print(list(adult))
def adults(x):
    if x > 18:
        return True
    return False

gasd = filter(adults, ages)
qwert = list(gasd)
print('AAA - ', qwert)
   # assert i < 78

# функция map
itog = list(map(lambda x: x * 2, ages))
print(itog)

# функция sorted
print(sorted(ages))

import math as m

r = 5
krug = 2*m.pi*r
print(krug)

print(m.sqrt(625))

print((m.pow(5, 6)))

print(m.hypot(5, 5))

