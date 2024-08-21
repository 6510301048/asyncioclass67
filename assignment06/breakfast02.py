import time
import asyncio

class Coffee:
    pass

class Egg:
    pass

class Bacon:
    pass

class Toast:
    pass

class Juice:
    pass

def PourCoffee():
    print(f"{time.ctime()} - Begin pour coffee...")
    time.sleep(2)
    print(f"{time.ctime()} - Finish pour coffee...")
    return Coffee()

async def ApplyButter():
    print(f"{time.ctime()} - Begin apply butter...")
    await asyncio.sleep(1)
    print(f"{time.ctime()} - Finish apply butter...")

async def FryEggs(eggs):
    print(f"{time.ctime()} - Begin fry eggs...")
    print(f"{time.ctime()} - Heat pan to fry eggs")
    await asyncio.sleep(1)
    for egg in range(eggs):
        print(f"{time.ctime()} - Frying", egg + 1, "eggs")
        await asyncio.sleep(1)
    print(f"{time.ctime()} - Finish fry eggs...")
    print(f"{time.ctime()} - >>>>>>>>> Fry eggs are ready...")
    return Egg()

async def FryBacon():
    print(f"{time.ctime()} - Begin fry bacon...")
    await asyncio.sleep(2)
    print(f"{time.ctime()} - Finish fry bacon...")
    print(f"{time.ctime()} - >>>>>>>>> Fry bacon is ready...")
    return Bacon()

async def ToastBread(slices):
    for slice in range(slices):
        print(f"{time.ctime()} - Toasting bread", slice + 1)
        await asyncio.sleep(1)
        print(f"{time.ctime()} - Bread", slice + 1, "toasted")
        await ApplyButter()
        print(f"{time.ctime()} - Toast", slice + 1, "ready")
    print(f"{time.ctime()} - >>>>>>>>> Toast are ready\n")
    return Toast()

def PourJuice():
    print(f"{time.ctime()} - Begin pour juice...")
    time.sleep(1)
    print(f"{time.ctime()} - Finish pour juice...")
    return Juice()

async def main():
    PourCoffee()
    print(f"{time.ctime()} - >>>>>>>>> Coffee is ready\n")
    tasks = [
        FryEggs(2),
        FryBacon(),
        ToastBread(2)
    ]
    await asyncio.gather(*tasks)
    print(f"{time.ctime()} - >>>>>>>>> Nearly to finished...\n")
    PourJuice()

if __name__ == "__main__":
    start_cooking = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start_cooking
    print(f"{time.ctime()} - Breakfast cooked in ", elapsed, "seconds.")


#     โค้ดนี้เป็นการจำลองกระบวนการทำอาหารเช้า โดยใช้การทำงานแบบอะซิงโครนัส (asynchronous) ผ่านไลบรารี `asyncio` ของ Python มาดูการทำงานของโค้ดนี้ทีละส่วนและอธิบายเป็นภาษาไทยกัน:

# ### 1. การสร้างคลาสต่างๆ
# - **`class Coffee`**, **`class Egg`**, **`class Bacon`**, **`class Toast`**, **`class Juice`**: คลาสเหล่านี้เป็นตัวแทนของส่วนประกอบอาหารเช้าต่างๆ (กาแฟ, ไข่, เบคอน, ขนมปังปิ้ง, และน้ำผลไม้) แต่ในที่นี้ไม่ได้มีการใช้งานคลาสเหล่านี้ในเชิงฟังก์ชันการทำงาน เพียงแค่เป็นตัวแทนในการคืนค่าในฟังก์ชันต่างๆ

# ### 2. ฟังก์ชันการเตรียมอาหาร
# - **`def PourCoffee()`**: เป็นฟังก์ชันซิงโครนัส (synchronous) ที่ทำการเทกาแฟ
#   - ใช้ `time.sleep(2)` เพื่อจำลองเวลาที่ใช้ในการเทกาแฟ 2 วินาที
#   - พิมพ์ข้อความเริ่มต้นและสิ้นสุดการเทกาแฟ และคืนค่ากาแฟ (เป็นวัตถุของคลาส `Coffee`)

# - **`async def ApplyButter()`**: เป็นฟังก์ชันอะซิงโครนัสที่ทาเนยบนขนมปัง
#   - ใช้ `await asyncio.sleep(1)` เพื่อจำลองการหน่วงเวลา 1 วินาที
#   - พิมพ์ข้อความเริ่มต้นและสิ้นสุดการทาเนย

# - **`async def FryEggs(eggs)`**: เป็นฟังก์ชันอะซิงโครนัสที่ทอดไข่
#   - ใช้ `await asyncio.sleep(1)` เพื่อจำลองการให้กระทะร้อนขึ้น
#   - ใช้ลูป `for` เพื่อทอดไข่ทีละฟอง โดยใช้เวลาฟองละ 1 วินาที (`await asyncio.sleep(1)`)
#   - พิมพ์ข้อความเมื่อเริ่มต้นทอดและเมื่อเสร็จสิ้นการทอดไข่
#   - คืนค่าไข่ที่ทอดเสร็จแล้ว (เป็นวัตถุของคลาส `Egg`)

# - **`async def FryBacon()`**: เป็นฟังก์ชันอะซิงโครนัสที่ทอดเบคอน
#   - ใช้ `await asyncio.sleep(2)` เพื่อจำลองเวลาที่ใช้ในการทอดเบคอน 2 วินาที
#   - พิมพ์ข้อความเมื่อเริ่มต้นและเสร็จสิ้นการทอดเบคอน
#   - คืนค่าเบคอนที่ทอดเสร็จแล้ว (เป็นวัตถุของคลาส `Bacon`)

# - **`async def ToastBread(slices)`**: เป็นฟังก์ชันอะซิงโครนัสที่ปิ้งขนมปัง
#   - ใช้ลูป `for` เพื่อปิ้งขนมปังแต่ละแผ่น โดยใช้เวลาปิ้งแผ่นละ 1 วินาที (`await asyncio.sleep(1)`)
#   - หลังจากปิ้งขนมปังแต่ละแผ่นแล้ว จะเรียกฟังก์ชัน `ApplyButter()` เพื่อทาเนยบนขนมปัง
#   - พิมพ์ข้อความเมื่อเริ่มต้นปิ้งและเมื่อเสร็จสิ้นการปิ้งขนมปัง
#   - คืนค่าขนมปังที่ปิ้งเสร็จแล้ว (เป็นวัตถุของคลาส `Toast`)

# - **`def PourJuice()`**: เป็นฟังก์ชันซิงโครนัสที่เทน้ำผลไม้
#   - ใช้ `time.sleep(1)` เพื่อจำลองเวลาที่ใช้ในการเทน้ำผลไม้ 1 วินาที
#   - พิมพ์ข้อความเริ่มต้นและสิ้นสุดการเทน้ำผลไม้ และคืนค่าน้ำผลไม้ (เป็นวัตถุของคลาส `Juice`)

# ### 3. ฟังก์ชันหลัก `main()`
# - **`async def main()`**: ฟังก์ชันหลักที่จัดการกระบวนการทำอาหารทั้งหมด
#   - เริ่มต้นด้วยการเรียกใช้ฟังก์ชัน `PourCoffee()` ซึ่งเป็นฟังก์ชันซิงโครนัสเพื่อเทกาแฟ
#   - สร้างรายการของงาน (tasks) ที่จะรันพร้อมกัน ได้แก่ `FryEggs(2)` (ทอดไข่ 2 ฟอง), `FryBacon()` (ทอดเบคอน), และ `ToastBread(2)` (ปิ้งขนมปัง 2 แผ่น)
#   - ใช้ `await asyncio.gather(*tasks)` เพื่อรอให้ทุกงานทำเสร็จสิ้น
#   - เมื่อทำอาหารหลักเสร็จแล้ว จะเรียกใช้ฟังก์ชัน `PourJuice()` เพื่อเทน้ำผลไม้

# ### 4. การเริ่มต้นโปรแกรม
# - โปรแกรมจะเริ่มต้นโดยการเรียกใช้ `asyncio.run(main())` ซึ่งจะรันฟังก์ชัน `main()` ที่จัดการกระบวนการทำอาหารเช้า
# - หลังจากฟังก์ชัน `main()` ทำงานเสร็จสิ้น จะพิมพ์เวลาที่ใช้ในการทำอาหารเช้า (ตั้งแต่เริ่มต้นจนถึงเสร็จสิ้น)

# ### ผลลัพธ์ที่คาดหวัง
# ผลลัพธ์จะมีลักษณะดังนี้ (ข้อความและเวลาจะแตกต่างกันไปตามเวลาที่ตั้งไว้ใน `time.sleep()` และ `asyncio.sleep()`):

# ```
# Wed Aug 14 06:00:00 2024 - Begin pour coffee...
# Wed Aug 14 06:00:02 2024 - Finish pour coffee...
# Wed Aug 14 06:00:02 2024 - >>>>>>>>> Coffee is ready

# Wed Aug 14 06:00:02 2024 - Begin fry eggs...
# Wed Aug 14 06:00:02 2024 - Heat pan to fry eggs
# Wed Aug 14 06:00:02 2024 - Begin fry bacon...
# Wed Aug 14 06:00:02 2024 - Toasting bread 1
# Wed Aug 14 06:00:03 2024 - Frying 1 eggs
# Wed Aug 14 06:00:03 2024 - Bread 1 toasted
# Wed Aug 14 06:00:03 2024 - Begin apply butter...
# Wed Aug 14 06:00:04 2024 - Finish apply butter...
# Wed Aug 14 06:00:04 2024 - Toast 1 ready
# Wed Aug 14 06:00:04 2024 - Toasting bread 2
# Wed Aug 14 06:00:04 2024 - Frying 2 eggs
# Wed Aug 14 06:00:05 2024 - Bread 2 toasted
# Wed Aug 14 06:00:05 2024 - Begin apply butter...
# Wed Aug 14 06:00:06 2024 - Finish apply butter...
# Wed Aug 14 06:00:06 2024 - Toast 2 ready
# Wed Aug 14 06:00:06 2024 - >>>>>>>>> Toast are ready

# Wed Aug 14 06:00:06 2024 - Finish fry eggs...
# Wed Aug 14 06:00:06 2024 - >>>>>>>>> Fry eggs are ready...
# Wed Aug 14 06:00:06 2024 - Finish fry bacon...
# Wed Aug 14 06:00:06 2024 - >>>>>>>>> Fry bacon is ready...
# Wed Aug 14 06:00:06 2024 - >>>>>>>>> Nearly to finished...

# Wed Aug 14 06:00:06 2024 - Begin pour juice...
# Wed Aug 14 06:00:07 2024 - Finish pour juice...
# Wed Aug 14 06:00:07 2024 - Breakfast cooked in  7.0 seconds.
# ```

# ผลลัพธ์แสดงว่ากาแฟถูกเทก่อน จากนั้นไข่, เบคอน และขนมปังถูกทำพร้อมกันแบบอะซิงโครนัส สุดท้ายน้ำผลไม้ถูกเทหลังจากอาหารหลักเสร็จสิ้น