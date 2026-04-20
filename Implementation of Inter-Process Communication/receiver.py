import multiprocessing
import time

def producer(pipe, name):
    for m in ["Message 1", "Message 2", "Message 3", "EXIT"]:
        print(f"{name} sending:", m)
        pipe.send(m)
        time.sleep(1)

def consumer(pipe, name):
    while True:
        m = pipe.recv()
        print(f"{name} received:", m)
        if m == "EXIT":
            print(f"{name} terminating")
            break

if __name__ == "__main__":
    p_conn, c_conn = multiprocessing.Pipe()

    p = multiprocessing.Process(target=producer, args=(p_conn, "Producer"))
    c = multiprocessing.Process(target=consumer, args=(c_conn, "Consumer"))

    p.start()
    c.start()

    p.join()
    c.join()