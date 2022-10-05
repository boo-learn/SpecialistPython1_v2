# =================================
#         Set (множество)
# =================================

print()
print('-= set =-')

# Множество — «контейнер», содержащий не повторяющиеся элементы в случайном порядке.

a = set()
print('a = ', a)  # set()

b = set(['a', 'b', 'c', 'c', 'a', 'e'])
print('b = ', b)

c = set('hello')
print('c = ', c)

d = {'a', 'b', 'c', 'd'}
print('d = ', d)

e = {i ** 2 for i in range(10)}  # генератор множеств
print('e = ', e)

f = {}  # А так получится словарь
print('type({}) -->', type(f))  # <class 'dict'>

# Операции с множествами

print(len(e))
print("'b' in b -->", 'b' in b)

# s == t
c1 = {'e', 'l', 'o', 'h'}
print(c == c1)

# s.issubset(t)	s <= t
print(c <= c1)

# s.issuperset(t)	s >= t
print(c >= {'h'})

# s.union(t, …)	s | t
print(b | d)

# s.intersection(t, …)	s & t
print(b & d)

# s.difference(t, …)	s - t
print(d - b)

# s.symmetric_difference(t)	s ^ t
print(d ^ b)

# s.copy()	
f = e
g = e.copy()

print('e:', id(e))
print('f:', id(f))
print('g:', id(g))

# Методы, изменяющие множества

# s.update(other, …)	s |= t
b |= d
print(b)

# s.intersection_update(t)	s &= t
b &= d
print(b)

# s.difference_update(t)	s -= t
b -= {'a', 'b'}
print(b)

# s.symmetric_difference_update(t)	s ^= t
b ^= c
print(b)

# s.add(elem)
b.add(1)
print(b)

# s.remove(elem)	
b.remove('h')
print(b)
# b.remove('z')

# s.discard(elem)
b.discard(1)
print(b)
b.discard('z')  # ошибки не возникает

# s.pop()
print(b.pop())
print(b)

# s.clear()	
b.clear()
print(b)

# ========================================
#     Frozenset (неизменяемое множество)
# ========================================

a = frozenset('hellow')
b = set('hellow')
print(a == b)
print(type(a - b))
print(type(b | a))
b.add('q')
# a.add('q') # вызовет ошибку
