import multiprocessing
import time

def producer(pipe, name):
    msgs = ["Message 1", "Message 2", "Message 3", "EXIT"]
    
    for m in msgs:
        msg = f"{name}: {m}"
        print(f"{name} sending:", m)
        pipe.send(msg)
        time.sleep(1)

if __name__ == "__main__":
    p1_conn, c1_conn = multiprocessing.Pipe()
    p2_conn, c2_conn = multiprocessing.Pipe()
    
    p1 = multiprocessing.Process(target=producer, args=(p1_conn, "Producer1"))
    p2 = multiprocessing.Process(target=producer, args=(p2_conn, "Producer2"))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("All messages sent")