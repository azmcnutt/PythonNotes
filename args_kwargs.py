from random import sample


def sample_function(*args, **kwargs):
    print(args)
    print(kwargs)
    print(args[2])
    print(kwargs['fifth'])
    
positional_arguments = ['first', 'second', 3]
keyword_arguments = {'forth': 'This is the forth', 'fifth': 'Not the forth'}

sample_function(*positional_arguments, **keyword_arguments)
sample_function('first','second',3,forth='This is the forth',fifth='Not the forth')