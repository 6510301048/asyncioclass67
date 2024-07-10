from random import random
import asyncio
import time

async def make_rice():
    await asyncio.sleep(random())
    start_time = time.time()
    await asyncio.sleep(1 + random())
    await asyncio.sleep(1)
    end_time = time.time()
    cook_time = end_time - start_time
    print(f"Rice: Cooking in {cook_time:.2f} seconds")
    return cook_time, 'Rice'

async def make_noodle():
    await asyncio.sleep(random())
    start_time = time.time()
    await asyncio.sleep(1 + random())
    await asyncio.sleep(1)
    end_time = time.time()
    cook_time = end_time - start_time
    print(f"Noodle: Cooking in {cook_time:.2f} seconds")
    return cook_time, 'Noodle'

async def make_curry():
    await asyncio.sleep(random())
    start_time = time.time()
    await asyncio.sleep(1 + random())
    await asyncio.sleep(1)
    end_time = time.time()
    cook_time = end_time - start_time
    print(f"Curry: Cooking in {cook_time:.2f} seconds")
    return cook_time, 'Curry'

# main coroutine
async def main():
    # create tasks with names
    rice_task = asyncio.create_task(make_rice(), name='Rice')
    noodle_task = asyncio.create_task(make_noodle(), name='Noodle')
    curry_task = asyncio.create_task(make_curry(), name='Curry')

    all_tasks = [rice_task, noodle_task, curry_task]

    # wait for the first task to complete
    done, pending = await asyncio.wait(all_tasks, return_when=asyncio.FIRST_COMPLETED)
    
    # report which task finished first and its cook time
    for task in done:
        cook_time, meal_name = await task  # get the return values from the task
    

    # wait for the rest of the tasks to complete
    await asyncio.wait(pending)

    print(f'Student A eat: {meal_name} (cooked in {cook_time:.2f} seconds)')

# start the asyncio program
asyncio.run(main())
