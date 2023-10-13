# Lists
my_list = [1, 2, 3, 4, 5]
print(my_list)

my_list.append(6)
print(my_list)

my_list.insert(2, 7)
print(my_list)

my_list.remove(3)
print(my_list)

print(len(my_list))

print(my_list[3])

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

print(my_tuple[2])

print(my_tuple.count(3))

# Sets
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

print(len(my_set))

# Dictionaries
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict)

print(my_dict['name'])

my_dict['age'] = 35
print(my_dict)

my_dict.pop('city')
print(my_dict)

print(len(my_dict))

# List comprehensions
my_list_comp = [x for x in range(10) if x % 2 == 0]
print(my_list_comp)

# Tuple unpacking
my_tuple_unpack = (1, 2, 3)
a, b, c = my_tuple_unpack
print(a, b, c)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

# Dictionary comprehensions
my_dict_comp = {x: x**2 for x in range(5)}
print(my_dict_comp)

# Nested data structures
nested = {'list': [1, 2, 3], 'tuple': (4, 5, 6), 'set': {7, 8, 9}, 'dict': {'name': 'Alice'}}
print(nested)

# Accessing nested elements
print(nested['list'][1])
print(nested['tuple'][2])
print(nested['set'].pop())
print(nested['dict']['name'])

# Slicing
my_list_slice = [1, 2, 3, 4, 5]
print(my_list_slice[1:4])
print(my_list_slice[::2])

# Sorting
my_list_sort = [5, 3, 1, 4, 2]
print(sorted(my_list_sort))

# Reversing
my_list_reverse = [1, 2, 3, 4, 5]
my_list_reverse.reverse()
print(my_list_reverse)

# Iterating
for item in my_list:
    print(item)

for key, value in my_dict.items():
    print(key, value)

# Checking membership
print(2 in my_list)
print(6 not in my_set)

# Checking emptiness
print(not my_tuple)
print(bool(my_dict))

# Clearing
my_list.clear()
print(my_list)

my_dict.clear()
print(my_dict
