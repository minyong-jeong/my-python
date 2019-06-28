import threading
import time

def example_func(name, sec):
    time.sleep(sec)
    print(name)

threads = []
items = [["thread1", 10], ["thread2", 3], ["thread3", 5]]

for item in items:
    processthread = threading.Thread(target=example_func,args=(item[0], item[1]))
    processthread.daemon=True
    threads.append(processthread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print('Done')
