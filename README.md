# PythonNotes
Things about Python I find interesting/didn't know and need to remember.

## Format strings:

    print('Old way: I completed %s tasks, in %s seconds.' % (num_tasks, time() - start_time))
    print(f'New way: I completed {num_tasks} tasks, in {time() - start_time} seconds.')

## *args and **kwargs

In a function, you can define *args and **kwargs as arguments (args and kwargs can be any characters, but we should stick with this standard).  *args is sent as a list of arguments.  Based on the number of arguments a programmer could perform different tasks.  **kwargs is sent as a dictionary of key value pairs.  These two are useful when the arguments of a function could change based on the action 

    def sample_function(*args, **kwargs):
        print(args)
        print(kwargs)
        print(args[2])
        print(kwargs['fifth'])
    
    positional_arguments = ['first', 'second', 3]
    keyword_arguments = {'forth': 'This is the forth', 'fifth': 'Not the forth'}

    sample_function(positional_arguments,keyword_arguments)
    sample_function('first','second',3,forth='This is the forth',fifth='Not the forth')

Will Output: 

    ('first', 'second', 3)
    {'forth': 'This is the forth', 'fifth': 'Not the forth'}
    3
    Not the forth
    ('first', 'second', 3)
    {'forth': 'This is the forth', 'fifth': 'Not the forth'}
    3
    Not the forth

