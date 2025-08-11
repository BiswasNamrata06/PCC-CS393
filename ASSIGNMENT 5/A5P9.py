data_set = {'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four', 'e': 'five', 'f': 'six'}
min_key = min(data_set, key=data_set.get)
print("Key with minimum value (alphabetically):", min_key)