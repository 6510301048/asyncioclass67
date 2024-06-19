# running a function in another thread
from time import sleep, ctime
from threading import Thread

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
