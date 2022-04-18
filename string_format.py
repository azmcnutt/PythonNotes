from time import time, sleep
from random import randrange

start_time = time()
num_tasks = randrange(1,10)
sleep(randrange(0,3))

print('Old way: I completed %s tasks, in %s seconds.' % (num_tasks, time() - start_time))
print(f'New way: I completed {num_tasks} taks, in {time() - start_time} seconds.')
