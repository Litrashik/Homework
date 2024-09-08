my_dict = {'Nikita': 1998, 'Anton': 2000, 'Kirill': 2002}
print(my_dict)
print(my_dict['Kirill'])
my_dict['Artem'] = 1996
print(my_dict)
my_dict.update({'Maria': 1999,
                'Valeria': 2000})
my_dict.pop('Anton')
print(my_dict)
my_set = {1, 1, 2, 2, 'String', 3, 4, 3, 4, True, 5.5, 'String', 5.5, False}
print(my_set)
my_set.add(7)
my_set.add('Russia')
my_set.discard(3)
print(my_set)
