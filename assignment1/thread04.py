# extending the Thread class and return values
from time import sleep, ctime
from threading import Thread

class CustomThread(Thread):
    #override the run function
    def run(self):
        #block for a moment
        sleep(1)
        #Display a message
        print(f'{ctime()} This is coming from another thread')
        #store return value
        self.value = 99

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
#get the value returned from run
value = thread.value
print(f'{ctime()} Got : {value}')