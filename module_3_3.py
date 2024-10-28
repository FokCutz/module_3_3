def print_params(a = 1, b = 'str', c = True):
    print(a , b , c)
    return

print_params()
print_params(1, 2)
print_params(1)
print_params(b = 25)
print_params(c = [1,2,3])

value_list = [True, 1.2, 'Hi']
values_dict = {'a': 5, 'b': 'строка', 'c': False}
print_params(*value_list)
print_params(**values_dict)

values_list_2 = [4.04, False]
print_params(*values_list_2, 42)

