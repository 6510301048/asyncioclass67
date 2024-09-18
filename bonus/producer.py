# https://aiokafka.readthedocs.io/en/stable/
import aiokafka
from aiokafka import AIOKafkaProducer
import asyncio
import json  # สำหรับแปลง dict เป็น bytes

async def send_one():
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')  # แปลง dict เป็น bytes
    )
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        while True:
            data = {"a": 123.4, "b": "some string"}
            # ส่งข้อมูลไปยัง Kafka โดยใช้ send_and_wait
            res = await producer.send_and_wait(topic="my_topic", value=data)
            print(f"Message sent: {res}")
            await asyncio.sleep(1)
    finally:
        # หยุด producer เมื่อเสร็จสิ้นการทำงาน
        await producer.stop()

# เริ่มรันฟังก์ชัน
asyncio.run(send_one())