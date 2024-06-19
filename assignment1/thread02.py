# running a function with arguments in another thread
# running a function with arguments in another thread
from time import sleep ,ctime
from threading import Thread

#a custom function that blocks for a moment
def task(sleep_time,message):
    #block for a moment
    sleep(sleep_time)
    #display a message
    print(f'{ctime()}{message}' )

#Create a thread
thread = Thread(target=task,args=(1.5, 'New message from another thread'))
#Run the thread
thread.start()
#Wait for the thread to finish 
print(f'{ctime()} Waiting for the thread...')
thread.join() 