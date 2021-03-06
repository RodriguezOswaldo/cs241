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

# to copy a list and re-use
fish_2 = fish.copy()
print(fish_2)

# reverse the order of the list
fish.reverse()
print(fish)

# get the number of elements in a list with the same value
print(fish.count('goby'))

# sort lists
fish.sort()
print(fish)

#
