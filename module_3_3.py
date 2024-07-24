def print_params(a=75, b='Alex', c=True):
    print(a, b, c)

#print_params('Den', 'Egor', 14, 3.68) ошибка, парметров больше указанных!
#print_params(13, 2) ошибка, параметров меньше указанных!
print_params()
print_params(b=25)
print_params(c=[1,2,3])

values_list = [4, 2.7, False]
print_params(*values_list)

values_dict = {'a': 34, 'b': 'Pol', 'c': 3.75}
print_params(**values_dict)

values_list_2 =['Max', 9]
print_params(*values_list_2, 42)

