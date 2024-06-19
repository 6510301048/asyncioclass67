# extending the Thread class
# running a function with arguments in another thread
from time import sleep, ctime
from threading import Thread

#custom thread class
class CustomThread(Thread):
    #override the run function
    def run(self):
        #block for a moment
        sleep(1)
        #Display a message
        print(f'{ctime()} This is coming from another thread')

#Create a thread
thread = CustomThread()
#Run the thread
thread.start()
'''
Thread 2nd
'''

#Wait for the thread to finish 
print(f'{ctime()} Waiting for the thread to finish') #ทำงานเลยไม่รอ
thread.join()