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



#     โค้ดที่คุณให้มาแสดงการใช้ไลบรารี `asyncio` ของ Python เพื่อรันงานอะซิงโครนัส (asynchronous) สำหรับการจำลองการเล่นหมากรุกกับคู่ต่อสู้หลายๆ คนพร้อมกัน มาดูการทำงานของโค้ดทีละส่วนและอธิบายเป็นภาษาไทยกัน:

# ### 1. การตั้งค่าพารามิเตอร์
# - **`my_compute_time = 0.1`**: เวลาในการคิดของ Judit (ผู้เล่นหลัก) ต่อการเคลื่อนที่หนึ่งครั้ง ใช้เวลา 0.1 วินาที
# - **`opponent_compute_time = 0.5`**: เวลาในการคิดของคู่ต่อสู้ต่อการเคลื่อนที่หนึ่งครั้ง ใช้เวลา 0.5 วินาที
# - **`opponents = 24`**: จำนวนคู่ต่อสู้ทั้งหมด 24 คน
# - **`move_pair = 30`**: จำนวนครั้งที่เคลื่อนที่บนกระดานหมากรุกแต่ละกระดาน (ผู้เล่น 1 ครั้งและคู่ต่อสู้ 1 ครั้ง = 1 ครั้ง)

# ### 2. ฟังก์ชัน `main(x)`
# - ฟังก์ชันนี้เป็นฟังก์ชันอะซิงโครนัสที่จะจำลองการเล่นหมากรุกกับคู่ต่อสู้ 1 คนบนกระดานที่ระบุด้วย `x`
# - **`board_start_time = time.perf_counter()`**: บันทึกเวลาที่เริ่มต้นเล่นกระดานนั้นๆ
# - มีลูปที่รัน **`for i in range(move_pair)`** เพื่อจำลองการเล่นทั้งหมด 30 ครั้ง (ผู้เล่นเคลื่อนที่ 30 ครั้ง คู่ต่อสู้เคลื่อนที่ 30 ครั้ง)
# - **`time.sleep(my_compute_time)`**: จำลองการคิดของผู้เล่นโดยหน่วงเวลา 0.1 วินาที (คำสั่งนี้เป็น synchronous ซึ่งจะบล็อก event loop)
# - พิมพ์ข้อความว่า Judit ได้เคลื่อนที่แล้ว
# - **`await asyncio.sleep(opponent_compute_time)`**: จำลองการคิดของคู่ต่อสู้โดยใช้เวลาหน่วง 0.5 วินาที (คำสั่งนี้เป็น asynchronous ซึ่งไม่บล็อก event loop)
# - พิมพ์ข้อความว่าคู่ต่อสู้ได้เคลื่อนที่แล้ว
# - หลังจากเคลื่อนที่ทั้งหมดเสร็จสิ้น จะพิมพ์เวลาที่ใช้ทั้งหมดในการเล่นกระดานนั้นและคืนค่าเวลาที่ใช้

# ### 3. ฟังก์ชัน `async_io()`
# - ฟังก์ชันนี้เป็นฟังก์ชันอะซิงโครนัสที่จัดการการเล่นพร้อมกันบนกระดานทั้งหมด
# - สร้างรายการของงาน (tasks) โดยเรียกใช้ฟังก์ชัน `main(i)` สำหรับคู่ต่อสู้แต่ละคน (24 คน)
# - **`await asyncio.gather(*tasks)`**: รอให้กระดานทั้งหมดเล่นเสร็จสิ้นพร้อมกัน
# - พิมพ์เวลาที่ใช้ทั้งหมดในการเล่นบนกระดานทั้งหมด

# ### 4. ส่วนหลักของโปรแกรม
# - โปรแกรมจะเริ่มด้วยการบันทึกเวลาที่เริ่มต้น (`start_time = time.perf_counter()`)
# - รันฟังก์ชัน `async_io()` โดยใช้ `asyncio.run(async_io())`
# - หลังจากการเล่นทั้งหมดเสร็จสิ้น จะพิมพ์เวลาที่ใช้ทั้งหมดในการเล่นหมากรุกกับคู่ต่อสู้ทั้งหมด

# ### การทำงานของโปรแกรม
# 1. โปรแกรมจะเริ่มเล่นหมากรุกกับคู่ต่อสู้ 24 คนพร้อมกัน โดยแต่ละกระดานมีการเล่นทั้งหมด 30 ครั้ง (คู่ต่อสู้แต่ละคนคิด 0.5 วินาทีต่อการเคลื่อนที่ครั้งเดียว)
# 2. ผู้เล่น (Judit) จะคิด 0.1 วินาทีต่อการเคลื่อนที่แต่ละครั้ง และคู่ต่อสู้จะคิด 0.5 วินาที
# 3. การทำงานของแต่ละกระดานจะทำงานแบบอะซิงโครนัส ทำให้โปรแกรมสามารถจัดการหลายกระดานพร้อมกันได้
# 4. หลังจากการเล่นทั้งหมดเสร็จสิ้น จะมีการพิมพ์เวลาที่ใช้ในการเล่นหมากรุกกับคู่ต่อสู้ทั้งหมด

# ### ผลลัพธ์ที่คาดหวัง
# โปรแกรมนี้จะใช้เวลาใกล้เคียงกับ 18 วินาทีในการเล่นหมากรุกกับคู่ต่อสู้ 24 คน หากไม่บล็อก event loop และดำเนินการทุกอย่างพร้อมกัน (เนื่องจากการคิดของคู่ต่อสู้ใช้เวลา 0.5 วินาทีต่อการเคลื่อนที่ และมี 30 ครั้งในการเล่นแต่ละครั้ง).