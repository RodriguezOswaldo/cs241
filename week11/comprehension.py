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

