# Synchronous cooking
# 2 kitchen 2 chefs 2 dishes

# Synchronous cooking
# 2 kitchen 2 chefs 2 dishes
from time import sleep, ctime, time

#cooking synchronous 
def cooking(index):
    print(f'{ctime()} Kitchen-{index} : Begin cooking...')
    sleep(2)
    print(f'{ctime()} Kitchen-{index} : Cooking done!...')

if __name__=="__main__":
    #Begin of main thread
    print(f'{ctime()} Main : Start cooking.')
    start_time = time() #จับเวลาในบรรทัดที่ 14 

    #Cooking for each dish
    for index in range(2): # number of cooking
        cooking(index)

    duration = time() - start_time
    print(f'{ctime()} Main : Finished cooking duration in {duration:0.2f} second')