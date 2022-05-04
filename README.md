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

    sample_function(*positional_arguments,**keyword_arguments)
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

## CSV Writer:

[X] is the delimiter, such as ',', or '\t' (for tab)
data is a list of values in a list, like:

    data = [
        ['first', 'last', 'email'],
        ['john', 'smith', 'johnsmith@somedomain.com']',
        etc.
    ]
    with open('new_data.cwsv', 'w') as new_csv:
        csv_writer = csv.writer(new_csv, '[X]'
        for line in data:
            csv_writer.writerow(line)

## Unit Testing

First step is to create a new file that starts with test_...py

Testing uses assertions:

    assertEqual(a, b)
        a == b
    assertNotEqual(a, b)
        a != b
    assertTrue(x)
        bool(x) is True
    assertFalse(x)
        bool(x) is False
    assertIs(a, b)
        a is b
    assertIsNot(a, b)
        a is not b
    assertIsNone(x)
        x is None
    assertIsNotNone(x)
        x is not None
    assertIn(a, b)
        a in b
    assertNotIn(a, b)
        a not in b
    assertIsInstance(a, b)
        isinstance(a, b)
    assertNotIsInstance(a, b)
        not isinstance(a, b)
    assertRaises([Error],[function],[args]

File format:

    import unittest
    import [module to be tested]
    
    @classmethod
    def setUpClass(cls):
        #will only run one before all tests
    
    @classmethod
    def tearDownClass(cls):
        # will only run one at the end of all tests
    
    def setUp(self):
        # will run before every test
        self.someClassorVariable
    
    def tearDown(self):
        # will run after every test
    
    class Test[ModuleName](unittest.TestCase):
        
        test_[function_to_test](self):
            self.assertEqual([function_to_test]([some input]),[expected answer])
            self.assetEeual(self.someClassorVariable, [expected])
            with assetRaises([Error]):
                [function]([args])
    
    # to automatically run the unit test from the IDE
    
    if __name__ == '__main__':
        unittest.main()

### Mocking

from: Cory Schafer's Python Tutorial: Unit Testing You Code wityh unittest module - https://youtu.be/6tNS--WetLI?t=1722

    from unittest.mock import patch
    def [a test]:
        with patch('module.request.get') as mocked_get:
            mocked_get.return_value.ok=true
            mocked_get.return_value.text = "success'

## Default Values of Functions

If a variable for a function has a mutable data type default, the default value is computed when the function is interpreted by the compiler, now each time the function is run. for instance:

    def show_time(time=datetime.now()):
        print(time.strftime('%B %d, %Y %H:%M:%S'))
    show_time()
    time.sleep(10)
    show_time()
 
 When executed this code will print the same time for both show_time calls, even though there is a ten second sleep.
 
 
            

# Credits

## Corey Schafer's YouTube Chanel Play List: Python Programming Beginner Tutorials

https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7
            
            
    
            
            
