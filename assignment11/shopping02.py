import time
import asyncio
from asyncio import Queue
from random import randrange

# we first implement the Customer and Product classes, 
# representing customers and products that need to be checked out. 
# The Product class has a checkout_time attribute, 
# which represents the time required for checking out the product.
class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products

# we implement a checkout_customer method that acts as a consumer.
# As long as there is data in the queue, this method will continue to loop. 
# During each iteration, it uses a get method to retrieve a Customer instance. 
# 
# If there is no data in the queue, it will wait. 
# 
# After retrieving a piece of data (in this case, a Customer instance), 
# it iterates through the products attribute and uses asyncio.sleep to simulate the checkout process.
# 
# After finishing processing the data, 
# we use queue.task_done() to tell the queue that the data has been successfully processed.
async def checkout_customer(queue: Queue, cashier_number: int):
    cashier_take = {"id": cashier_number, "customer": 0, "time": 0.0}  # 1. Initialize a dictionary for each cashier

    while not queue.empty():
        customer: Customer = await queue.get()
        customer_start_time = time.perf_counter()
        print(f'The cashier_{cashier_number} will checkout Customer_{customer.customer_id}')

        for product in customer.products:
            product_take_time = round(product.checkout_time, ndigits=2)
            print(f"The cashier_{cashier_number} will checkout customer_{customer.customer_id}'s "
                  f"Product_{product.product_name} for {product.checkout_time} secs")
            await asyncio.sleep(product_take_time)
            cashier_take["time"] += product_take_time  # 2. Add the product checkout time

        print(f"The cashier_{cashier_number} finished checkout for customer_{customer.customer_id} "
              f"in {round(time.perf_counter() - customer_start_time, ndigits=2)} secs")

        cashier_take["customer"] += 1  # 3. Increment the number of customers processed
        queue.task_done()

    return cashier_take  # 4. Return the result for this cashier

# we implement the generate_customer method as a factory method for producing customers.
#
# We first define a product series and the required checkout time for each product. 
# Then, we place 0 to 4 products in each customer’s shopping cart.
def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)

# we implement the customer_generation method as a producer. 
# This method generates several customer instances regularly 
# and puts them in the queue. If the queue is full, the put method will wait.
async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id)
                     for the_id in range(customer_count, customer_count+customers)]
        for customer in customers:
            print("Waiting to put customer in line.....")
            await queue.put(customer)
            print("cCustomer put in line.....")
        customer_count = customer_count + len(customers)
        await asyncio.sleep(.001)
        return customer_count
# Finally, we use the main method to initialize the queue, 
# producer, and consumer, and start all concurrent tasks.
async def main():
    customer_queue = Queue(2)
    customer_start_time = time.perf_counter()
    customer_product = asyncio.create_task(customer_generation(customer_queue, 2))
    cashiers = [checkout_customer(customer_queue, i) for i in range(2)]
    result = await asyncio.gather(customer_product, *cashiers)

    print (20*'-')
    for cashier in result[1:]: #Since the 1 position -> 0 1 2...
        if cashier:
            print(f"The cashier_{cashier['id']}"
                  f"take {cashier['customer']} customers"
                  f"total {round(cashier['time'], ndigits=2)} secs")
            
    print(f"The supermaket process finished"
          f"{result[0]} customers"
            f"in{round(time.perf_counter() - customer_start_time, ndigits=2)} secs")   
if __name__ == "__main__":
    asyncio.run(main())



'''
-------------------------------------------------------------------------------------------
|  Customer | Queue |  Cashier  |        Customers/time by Cashier                | Total |
-------------------------------------------------------------------------------------------
|           |       |           |C  |0    |C  |1    |C  |2    |C  |3    |C  |4    |       |
-------------------------------------------------------------------------------------------
|     2     |   2   |     2     |1  |2.0s |1  |2.0s |   |     |   |     |   |     | 2.01s |
-------------------------------------------------------------------------------------------
|     3     |   2   |     2     |2  |4.0s |1  |2.0s |   |     |   |     |   |     | 4.01s |
-------------------------------------------------------------------------------------------
|     4     |   2   |     2     |2  |4.0s |2  |4.0s |   |     |   |     |   |     | 4.01s |
-------------------------------------------------------------------------------------------
|     5     |   5   |     5     |5  |2.0s |1  |2.0s |1  |2.0s |1  |2.0s |   |     | 2.01s |
-------------------------------------------------------------------------------------------
|     10    |   3   |     3     |3  |8.0s |3  |6.0s |3  |6.0s |   |     |   |     | 8.03s |
-------------------------------------------------------------------------------------------
|     10    |   3   |     5     |5  |8.0s |3  |6.0s |3  |6.0s |   |     |   |     | 8.02s |
-------------------------------------------------------------------------------------------
|     20    |   5   |     5     |5  |8.0s |4  |8.0s |4  |8.0s |   |8.0s |   |     | 8.02s |
-------------------------------------------------------------------------------------------
'''