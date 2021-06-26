fish = ['barracuda', 'cod', 'devil ray', 'eel']

# insert item at the end of the list
fish.append('flounder')

print(fish)

# insert item at specified index
fish.insert(0, 'owner')

print(fish)

more_fish = ['goby', 'herring', 'ide', 'kissing gourami']

# Add a second lists to an existing lists
fish.extend(more_fish)
print(fish)

# Removing one item from the list
fish.remove('kissing gourami')
print(fish)

# remove the last item in the list or the one in the specified index
print(fish.pop(3))
print(fish)