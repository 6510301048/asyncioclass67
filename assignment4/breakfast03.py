# Asynchronous breakfast
import asyncio
from time import sleep, time

async def make_coffee(): #1
    print("coffee: prepare ingridients")
    sleep(1)
    print("coffee: waiting...")
    await asyncio.sleep(5) #2: pause, another tasks can be run 
    print("coffee: ready")

async def fry_eggs(): #1
    print("eggs: prepare ingridients")
    sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3) #
    print("eggs: ready")

async def main():
    start = time()
    coffee_task = asyncio.create_task(make_coffee())
    egg_task = asyncio.create_task(fry_eggs())
    await coffee_task
    await egg_task
    print(f"breakfast is ready in {time()-start} min")

asyncio.run(main()) 


# โค้ดที่คุณให้มาแสดงการใช้ไลบรารี `asyncio` ของ Python เพื่อรันงานแบบอะซิงโครนัส (asynchronous) พร้อมกัน เรามาแยกส่วนของโค้ดและอธิบายการทำงานกัน:

# ### 1. ฟังก์ชัน `make_coffee` และ `fry_eggs`
# - **`make_coffee()`** และ **`fry_eggs()`** เป็นฟังก์ชันอะซิงโครนัส (ซึ่งระบุด้วยคำว่า `async` ข้างหน้า)
# - ทั้งสองฟังก์ชันมีรูปแบบการทำงานคล้ายกัน:
#   - พิมพ์ข้อความเพื่อบอกว่ากำลังเริ่มเตรียมการ
#   - เรียกใช้ฟังก์ชัน `sleep(1)` เพื่อจำลองการหน่วงเวลาซิงโครนัส (synchronous delay) อย่างไรก็ตาม การเรียกใช้ฟังก์ชันนี้จะบล็อกการทำงาน และควรเปลี่ยนเป็น `await asyncio.sleep(1)` เพื่อให้ไม่บล็อกการทำงานของโปรแกรม
#   - จากนั้นจะจำลองการหน่วงเวลาแบบอะซิงโครนัสโดยใช้ `await asyncio.sleep(5)` สำหรับกาแฟ และ `await asyncio.sleep(3)` สำหรับไข่
#   - หลังจากหน่วงเวลาแล้วจะพิมพ์ข้อความว่าอาหารพร้อมแล้ว

# ### 2. ฟังก์ชัน `main`
# - **`main()`** เป็นฟังก์ชันอะซิงโครนัสที่ทำหน้าที่เป็นหลักในการทำงาน
# - โปรแกรมจะบันทึกเวลาเริ่มต้นโดยใช้ `time()`
# - มีการสร้างงาน (tasks) สองงานโดยใช้ `asyncio.create_task()`:
#   - `coffee_task` รัน `make_coffee()`
#   - `egg_task` รัน `fry_eggs()`
# - จากนั้นโปรแกรมจะรอให้งานทั้งสองงานเสร็จสิ้นโดยใช้ `await coffee_task` และ `await egg_task`
# - สุดท้ายโปรแกรมจะคำนวณและพิมพ์เวลารวมที่ใช้ในการเตรียมอาหารเช้า

# ### 3. `asyncio.run(main())`
# - บรรทัดนี้จะรันฟังก์ชัน `main()` และจัดการ event loop ซึ่งเป็นจุดเริ่มต้นของโปรแกรมอะซิงโครนัส

# ### ลำดับการทำงาน
# 1. โปรแกรมเริ่มฟังก์ชัน `main()` และบันทึกเวลาเริ่มต้น
# 2. `make_coffee()` และ `fry_eggs()` ถูกกำหนดให้เป็นงานที่จะรันพร้อมกัน
# 3. โปรแกรมจะพิมพ์ข้อความเตรียมการสำหรับทั้งกาแฟและไข่
# 4. โปรแกรมจะเข้าสู่ช่วงเวลาที่จะหน่วงการทำงานแบบอะซิงโครนัส (`await asyncio.sleep(...)`) ซึ่งในช่วงนี้ event loop จะสลับระหว่างงานต่างๆ
# 5. หลังจากหน่วงเวลาทั้งหมดเสร็จสิ้น โปรแกรมจะพิมพ์ข้อความว่ากาแฟและไข่พร้อมแล้ว
# 6. สุดท้ายโปรแกรมจะพิมพ์เวลารวมที่ใช้ในการเตรียมอาหารเช้า

# ### ซิงโครนัส (Synchronous) กับ อะซิงโครนัส (Asynchronous)
# - การเรียกใช้ `sleep(1)` เป็นแบบซิงโครนัสและจะบล็อก event loop ซึ่งไม่เหมาะสมในโปรแกรมแบบอะซิงโครนัส ควรเปลี่ยนเป็น `await asyncio.sleep(1)` เพื่อให้โปรแกรมทำงานได้โดยไม่ถูกบล็อก

# ### ตัวอย่างผลลัพธ์
# หากเปลี่ยนการเรียกใช้ `sleep(1)` เป็น `await asyncio.sleep(1)` จะได้ผลลัพธ์ประมาณนี้:
# ```
# coffee: prepare ingredients
# eggs: prepare ingredients
# coffee: waiting...
# eggs: frying...
# eggs: ready
# coffee: ready
# breakfast is ready in 6.01 min
# ```

# หากไม่เปลี่ยนการเรียกใช้ `sleep(1)` โปรแกรมจะรันอย่างซิงโครนัสในช่วงหน่วงเวลา 1 วินาที ทำให้ประสิทธิภาพลดลง