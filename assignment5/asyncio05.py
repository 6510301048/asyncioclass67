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




# โค้ดที่คุณให้มาแสดงการใช้ไลบรารี `asyncio` ของ Python เพื่อรันงานแบบอะซิงโครนัส (asynchronous) โดยในตัวอย่างนี้เป็นการจำลองการทำอาหาร 3 อย่าง ได้แก่ ข้าว (Rice), ก๋วยเตี๋ยว (Noodle) และแกง (Curry) จากนั้นจะตรวจสอบว่าอาหารชนิดไหนทำเสร็จก่อน มาดูการทำงานของโค้ดทีละส่วนและอธิบายเป็นภาษาไทยกัน:

# ### 1. ฟังก์ชันการทำอาหาร (`make_rice`, `make_noodle`, `make_curry`)
# - ฟังก์ชันเหล่านี้เป็นฟังก์ชันอะซิงโครนัสที่ใช้ `async` และ `await` ในการจัดการการทำงาน
# - **`await asyncio.sleep(random())`**: จำลองการหน่วงเวลาที่สุ่มขึ้นมาสำหรับการเริ่มต้นทำอาหาร (เพื่อให้แต่ละงานเริ่มต้นที่เวลาต่างกัน)
# - **`start_time = time.time()`**: บันทึกเวลาเริ่มต้นการทำอาหาร
# - **`await asyncio.sleep(1 + random())`** และ **`await asyncio.sleep(1)`**: จำลองการทำอาหารโดยใช้เวลาสุ่มตามด้วยเวลา 1 วินาที
# - **`end_time = time.time()`**: บันทึกเวลาที่สิ้นสุดการทำอาหาร
# - **`cook_time = end_time - start_time`**: คำนวณเวลาที่ใช้ในการทำอาหาร
# - พิมพ์ข้อความบอกเวลาที่ใช้ในการทำอาหาร และคืนค่าเวลาและชื่อของอาหารที่ทำเสร็จ

# ### 2. ฟังก์ชันหลัก `main()`
# - ฟังก์ชันนี้เป็นฟังก์ชันอะซิงโครนัสที่จัดการการทำอาหารทั้งหมด
# - **`rice_task = asyncio.create_task(make_rice(), name='Rice')`**: สร้างงานอะซิงโครนัสสำหรับการทำข้าว
# - **`noodle_task = asyncio.create_task(make_noodle(), name='Noodle')`**: สร้างงานอะซิงโครนัสสำหรับการทำก๋วยเตี๋ยว
# - **`curry_task = asyncio.create_task(make_curry(), name='Curry')`**: สร้างงานอะซิงโครนัสสำหรับการทำแกง
# - **`all_tasks = [rice_task, noodle_task, curry_task]`**: สร้างรายการที่รวมงานทั้งหมด
# - **`done, pending = await asyncio.wait(all_tasks, return_when=asyncio.FIRST_COMPLETED)`**: รอให้งานแรกในรายการทำเสร็จ โดยงานที่เสร็จจะถูกบรรจุใน `done` และงานที่ยังไม่เสร็จจะถูกบรรจุใน `pending`
# - ในลูป **`for task in done:`**: ดึงค่าที่คืนมาจากงานที่ทำเสร็จแล้ว โดยค่าที่คืนมาคือ `cook_time` (เวลาที่ใช้ในการทำอาหาร) และ `meal_name` (ชื่อของอาหาร)
# - **`await asyncio.wait(pending)`**: รอให้งานที่เหลือทั้งหมดทำเสร็จ
# - พิมพ์ข้อความบอกชื่อของอาหารที่ทำเสร็จก่อนและเวลาที่ใช้ในการทำ

# ### 3. การเริ่มต้นโปรแกรม
# - โปรแกรมจะเริ่มโดยการเรียกใช้ฟังก์ชัน `asyncio.run(main())` ซึ่งจะรันฟังก์ชัน `main()` ที่จัดการการทำงานทั้งหมด

# ### การทำงานของโปรแกรม
# 1. โปรแกรมจะเริ่มทำอาหาร 3 อย่างพร้อมกัน ได้แก่ ข้าว, ก๋วยเตี๋ยว, และแกง โดยใช้เวลาในการทำที่แตกต่างกัน (แบบสุ่ม)
# 2. โปรแกรมจะตรวจสอบว่าอาหารชนิดใดทำเสร็จก่อน และแสดงชื่อของอาหารนั้นพร้อมกับเวลาที่ใช้ในการทำ
# 3. โปรแกรมจะรอให้อาหารชนิดอื่นๆ ทำเสร็จทั้งหมดก่อนจะสิ้นสุดการทำงาน

# ### ผลลัพธ์ที่คาดหวัง
# ตัวอย่างผลลัพธ์ที่ได้อาจมีลักษณะดังนี้ (ผลลัพธ์อาจแตกต่างกันไปเพราะเวลาที่ใช้ในการทำอาหารแต่ละชนิดถูกสุ่มขึ้นมา):
# ```
# Rice: Cooking in 2.12 seconds
# Curry: Cooking in 2.20 seconds
# Noodle: Cooking in 2.40 seconds
# Student A eat: Rice (cooked in 2.12 seconds)
# ``` 

# ในตัวอย่างนี้ ข้าว (Rice) ทำเสร็จก่อนและใช้เวลา 2.12 วินาที จากนั้นโปรแกรมจะพิมพ์ว่า "Student A eat: Rice (cooked in 2.12 seconds)"