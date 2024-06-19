import concurrent.futures
import logging
import time

class FakeDatabase:
    def __init__(self):  # Correct constructor method
        self.value = 0

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        with self._lock:  # Using the lock to ensure only one thread updates at a time
            localcopy = self.value
            localcopy += 1
            time.sleep(0.1)
            self.value = localcopy
        logging.info("Thread %s: finishing update", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for index in range(2):
            executor.submit(database.update, index)

    logging.info("Testing update. Ending value is %d.", database.value)
