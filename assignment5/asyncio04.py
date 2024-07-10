# example of waiting for all tasks to be completed with a timeout

from random import random 
import asyncio

#coroutine to execute in a new task
async def task_coro(arg):
    #generate a random value between 0 and 1
    value = random ()
    #block for a moment
    await asyncio.sleep(value)
    #report the value
    print (f'>task {arg}done with {value}')
  
#main coroutine
async def main():
    #create many tasks
    task = [asyncio.create_task(task_coro(i)) for i in range(10)]
# wait for the first task to complete
    done, pending = await asyncio.wait(task, timeout=5)
    #report result
    print(f'Done,{len(done)}tasks completed in time')
    
# start  the asyncio program
asyncio.run(main())