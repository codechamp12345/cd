import time

processes = [0, 1, 2]
timestamps = [2, 1, 3]

queue = list(zip(timestamps, processes))
queue.sort()

print("Request Queue:", queue)

for t, p in queue:
    print(f"P{p} sends REQUEST at time {t}")
    
    # simulate replies from others
    for other in processes:
        if other != p:
            print(f"P{other} sends REPLY to P{p}")
    
    print(f"P{p} ENTERING CS")
    time.sleep(1)
    print(f"P{p} EXITING CS\n")

print("All processes completed")