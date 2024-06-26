# running a function in another thread
from time import sleep, ctime
from threading import Thread

<<<<<<< HEAD
#a custom function that blocks for a moment
def task():
    #block for a moment
    sleep(1)
    #display a message
    print(f'{ctime()} This is from another thread')

#Create a thread
thread = Thread(target=task)
#Run the thread
thread.start()
#Wait for the thread to finish 
print(f'{ctime()} Waiting for the thread...')
thread.join() 
=======
# a custom function that blocks for a moment
def task():
    # block for a moment
    sleep(1)
    # display a message
    print(f'{ctime()} This is from another thread')

# create a thread
thread = Thread(target=task)
# run the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
thread.join()
>>>>>>> 3970926c92ff939fa8cee033ec5ab6e687e5eeab
