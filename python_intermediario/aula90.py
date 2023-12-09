import sys

# Generator expression, Iterables e Irerators em Python

iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable) #tem __iter__ e __next__
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

lista = [n for n in range (10000000)]
generator = (n for n in range (10000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)