def my_func():
    pass

A_name = 'A'
A_parents = (object,)
A_methods = {'a': 1 ,'my_func': my_func}

A = type(A_name, A_parents, A_methods)