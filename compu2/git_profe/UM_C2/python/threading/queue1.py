
import threading, queue

q = queue.Queue()
#q = queue.LifoQueue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# turn-on the worker thread
threading.Thread(target=worker, daemon=True).start()

# send thirty task requests to the worker
for item in range(30):
    print(f'Putting item {item}')
    q.put(item)
print('All task requests sent\n', end='')
print(f"Queue empty? -> {q.empty()}")
# block until all tasks are done
q.join()
print(f"Queue empty? -> {q.empty()}")
print('All work completed')
