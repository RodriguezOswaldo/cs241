from math import sin, cos, tan, pi

sums = lambda x, y: x + y
print(sums(3, 4))


def sum(x, y):
    return x + y


print(sum(3, 4))

# without lambda
def fahrenheit(T):
    return (float(9) / 5) * T + 32


def celcius(T):
    return (float(5)/9) * (T - 32)


temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)
C = map(celcius, temperatures)

temperatures_in_fahrenheit = list(map(fahrenheit, temperatures))
temperatures_in_celcius = list(map(fahrenheit, temperatures_in_fahrenheit))
print(temperatures_in_fahrenheit)
print(temperatures_in_celcius)
print('\n########\n')
# with lambda

C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9) / 5) * x + 32, C))
print(F)

C = list(map(lambda x: (float(5)/9) * (x-32), F))
print(C)

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
# map adds a function to one or more iterables, such as list, tuple, etc, in this case are lists, a, b, c.
me = list(map(lambda x, y, z: 2.5*x + 2*y - z, a, b, c))
print(me)

def map_functions(x, functions):
    """ map an interable of functions on the the object x """
    res = []
    for func in functions:
        res.append(func(x))
    return res


family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))

