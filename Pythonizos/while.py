start = 100
x = 0

while x <= 4:
    points = input('type in: ')
    if points == "hit":
        start += 10
    elif points == "miss":
        start -= 20
        x += 1

print(start)