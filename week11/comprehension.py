for x in range(10):
    x**2
s = [x**2 for x in range(10)]

for i in range(13):
    2**i
v = [2**i for i in range(13)]

print(s)
print(v)

S = [1, 2, 3, 4, 5, 6]
M = [x for x in S if x % 2 == 0]
print(M)


d = [x**3 for x in range(10)]
print(d)

# this is the same than
new_list = []
for n in range(10):
    if n % 2 == 0:
        new_list.append(n**2)
print(new_list)
# this (mind blowing)
second_list = [n**2 for n in range(10) if n % 2 == 0]
print(second_list)

"""
 More practice in list comprehensions
"""

squares = [n**3 for n in range(100)]
print(squares)


"""
numbers divisibles by 5 or 7
"""
mi_n = 1
# divisibles = [n for n in range(0, 99) if n % 5 == 0]
while mi_n != 0:
    mi_n = int(input('what number do you want to divide for?: \n'))
    if mi_n == 5:
        divisibles = [mi_n for mi_n in range(0, 99) if mi_n % 5 == 0]
        print(divisibles)
    else:
        divisibles_two = [mi_n for mi_n in range(0,99) if mi_n % 7 == 0]
        print(divisibles_two)