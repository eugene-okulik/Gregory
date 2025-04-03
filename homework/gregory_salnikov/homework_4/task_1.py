my_dict = {
    'tuple': (10, 4, 2, 'april', 'horse'),
    'list': [17, 11, 0, 'november', 'dragon'],
    'dict': {'day': 26, 'month': 1, 'year': 1966, 'monthname': 'january', 'yearname': 'horse'},
    'set': {20, 7, 71, 'july', 'pig'}
    }

key_tuple = my_dict['tuple']
print(key_tuple[-1])

key_list = my_dict['list']
key_list.append('new_element')
key_list.pop(1)

key_dict = my_dict['dict']
key_dict[('i am a tuple',)] = 'this is tuple'
key_dict.pop('year')

key_set = my_dict['set']
key_set.add(60)
key_set.remove(71)

print(my_dict)
