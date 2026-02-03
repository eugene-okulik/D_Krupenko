my_dict = {
    'tuple': (1, 2, 3, 4, 5, 6, 7),
    'list': [1, 2, 3, 4, 5, 6],
    'dict': {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
    'set': {1, 2, 3, 4, 5}
}
print(my_dict)
print(my_dict['tuple'][-1])
print(my_dict['list'])
my_dict['list'].append(7)
print(my_dict['list'])
my_dict['list'].pop(1)
print(my_dict['list'])
print(my_dict['dict'])
my_dict['dict'][('i am a tuple',)] = 6
print(my_dict['dict'])
my_dict['dict'].pop('three')
print(my_dict['dict'])
print(my_dict['set'])
my_dict['set'].add(6)
print(my_dict['set'])
my_dict['set'].discard(3)
print(my_dict['set'])
