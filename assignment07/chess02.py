import time
import asyncio

my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 24 #1 opponent = 18 sec
move_pair = 30

#Again notice that I declare the main() function as a async function
async def main(x):
    board_start_time = time.perf_counter()
    for i in range (move_pair):
        #print(f"BOARD-{x} {i+1} Judit thinking of make move")
        #Don't use time.sleep in a async function. I'm using it because in reality you aren't thinking about making move
        #Move on 24 boards at the same time, and so I need to block the event loop
        time.sleep(my_compute_time) #if it async every board will be 18
        print(f'BOARD-{x+1} {i+1} Judit made a move')
        #The opponent thinks for 5 seconds
        await asyncio.sleep(opponent_compute_time)
        print(f'BOARD-{x+1} {i+1} Opponents made move')
    print(f"BOARD- {x+1} - >>>>>>>>>>>>>> Finished move in {round (time.perf_counter() - board_start_time)}secs\n")
    return round(time.perf_counter() - board_start_time)

async def async_io():
    tasks = []
    for i in range(opponents):
        tasks += [main(i)]
    await asyncio.gather(*tasks)
    print(f"Board exhibition finished in {round(time.perf_counter() - start_time)} secs.")

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f'Finished in {round(time.perf_counter() - start_time)} secs.')