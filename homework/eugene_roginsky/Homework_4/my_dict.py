my_dict = {
    'tuple' : (5, 4, 3, True, 36.6),
    'list' : [10, 20, None, 30, 7],
    'dict' : {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5'},
    'set' : {1, 4, 'string', 5.6, True}
}
print(my_dict['tuple'][-1])
my_dict['list'].append(6)
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] =  'yes you are'
my_dict['dict'].pop(2)
my_dict['set'].add('new element')
my_dict['set'].pop()
print(my_dict)
