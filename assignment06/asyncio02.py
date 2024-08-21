import asyncio

#define an asynchronous iterrator
class AsyncIterator:

    #constructor, define some data
    def __init__(self):
        self.counter = 0
    
    #create an instance of the iterator
    def __aiter__(self):
        return self
    
    #return the next awaitable
    async def __anext__(self):
        #check for no further items
        if self.counter >= 10:
            raise StopAsyncIteration
        #increment the counter 
        self.counter += 1
        #simulate work
        await asyncio.sleep(1)
        #return the counter value
        return self.counter
    
#main coroutine
async def main():
    #loop over async iterator with async for loop
    async for item in AsyncIterator():
        print(item)

#Running the async main function
asyncio.run(main())


# โค้ดนี้แสดงตัวอย่างการสร้างตัววนซ้ำแบบอะซิงโครนัส (asynchronous iterator) ใน Python โดยใช้ `asyncio` และใช้งานผ่าน `async for` มาดูการทำงานของโค้ดนี้ทีละส่วนและอธิบายเป็นภาษาไทยกัน:

# ### 1. การสร้างคลาส `AsyncIterator`
# - **`class AsyncIterator:`**: คลาสนี้เป็นตัวแทนของตัววนซ้ำแบบอะซิงโครนัส
# - **`def __init__(self):`**: เมธอดนี้เป็นตัวสร้าง (constructor) ของคลาส ใช้ในการกำหนดค่าเริ่มต้นของตัวแปร `counter` ซึ่งเริ่มต้นที่ `0`
#   - `self.counter = 0`: ตัวแปร `counter` จะเก็บจำนวนครั้งที่วนซ้ำ

# - **`def __aiter__(self):`**: เมธอดนี้เป็นเมธอดที่ทำให้คลาสนี้สามารถใช้เป็นตัววนซ้ำได้ โดยการคืนค่าตัวมันเอง (`self`)

# - **`async def __anext__(self):`**: เมธอดนี้เป็นเมธอดที่ทำให้คลาสนี้สามารถทำงานแบบอะซิงโครนัสได้ และถูกเรียกใช้เพื่อคืนค่าถัดไปในลำดับ
#   - **`if self.counter >= 10:`**: ตรวจสอบว่าถ้าตัวแปร `counter` มีค่าเท่ากับหรือมากกว่า 10 ให้ยกเลิกการวนซ้ำโดยการโยนข้อยกเว้น `StopAsyncIteration` ซึ่งเป็นสัญญาณว่าการวนซ้ำสิ้นสุดลง
#   - **`self.counter += 1`**: เพิ่มค่าของ `counter` ขึ้น 1 ทุกครั้งที่มีการเรียกใช้เมธอดนี้
#   - **`await asyncio.sleep(1)`**: หน่วงเวลาการทำงานเป็นเวลา 1 วินาทีเพื่อจำลองการทำงานแบบอะซิงโครนัส
#   - **`return self.counter`**: คืนค่าปัจจุบันของ `counter` หลังจากการหน่วงเวลา

# ### 2. ฟังก์ชันหลัก `main()`
# - **`async def main():`**: ฟังก์ชันหลักนี้เป็นฟังก์ชันอะซิงโครนัส
#   - **`async for item in AsyncIterator():`**: ใช้ลูป `async for` เพื่อวนซ้ำผ่านวัตถุที่สร้างจากคลาส `AsyncIterator` ซึ่งจะรอผลลัพธ์จาก `__anext__` แต่ละรอบ ก่อนจะดำเนินการวนซ้ำต่อไป
#   - **`print(item)`**: พิมพ์ค่าที่ได้จาก `__anext__` ซึ่งในที่นี้คือค่าของ `counter`

# ### 3. การรันโปรแกรม
# - **`asyncio.run(main())`**: ใช้คำสั่งนี้เพื่อรันฟังก์ชันหลัก `main()` ซึ่งเป็นฟังก์ชันอะซิงโครนัส

# ### การทำงานของโปรแกรม
# เมื่อรันโปรแกรมนี้ ฟังก์ชัน `main()` จะทำงาน โดยลูป `async for` จะวนซ้ำทั้งหมด 10 ครั้ง (เพราะ `counter` ถูกกำหนดให้หยุดที่ 10) ในแต่ละรอบของการวนซ้ำ โปรแกรมจะหน่วงเวลา 1 วินาที ก่อนจะพิมพ์ค่าปัจจุบันของ `counter` ออกมา

# ### ผลลัพธ์ที่คาดหวัง
# ผลลัพธ์ที่ได้จากโปรแกรมจะเป็นลำดับของตัวเลขตั้งแต่ 1 ถึง 10 โดยแต่ละบรรทัดจะมีช่วงเวลา 1 วินาทีระหว่างกัน:

# ```
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# ```

# โค้ดนี้แสดงให้เห็นถึงการใช้งาน `async for` เพื่อทำการวนซ้ำแบบอะซิงโครนัส ซึ่งช่วยให้สามารถจัดการกับงานที่ต้องรอเวลา (เช่น การเชื่อมต่อเครือข่ายหรือการทำงานอื่นๆ ที่ต้องใช้เวลานาน) ได้อย่างมีประสิทธิภาพมากขึ้น