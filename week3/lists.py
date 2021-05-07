cars = []

cars.append("Ford")
cars.append("Mazda")
cars.append("Dodge")
cars.insert(0, "Toyota")


for i in cars:
    if i == 'Toyota':
        print(f'Your car is a {i}')
    elif i == 'Mazda':
        print(f'I can\'t believe you bought a {i}')
    elif i == 'Dodge':
        print(f'{i} is my favorite car to hit the road with')
    elif i == 'Ford':
        print(f'Meh, I am not too interested in a {i}')