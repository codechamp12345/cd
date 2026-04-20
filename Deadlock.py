lock = {}
wait = {}

def detect_cycle():
    visited = set()
    stack = set()

    def dfs(p):
        if p in stack:
            return True
        if p in visited:
            return False

        visited.add(p)
        stack.add(p)

        if p in wait:
            if dfs(wait[p]):
                return True

        stack.remove(p)
        return False

    for p in wait:
        if dfs(p):
            return True
    return False


def request(p, f):
    if f in lock:
        print(f"{p} waiting for {f} (held by {lock[f]})")
        wait[p] = lock[f]

        if detect_cycle():
            print("Deadlock detected! Resolving...")
            release(p)
    else:
        print(f"{p} acquired {f}")
        lock[f] = p


def release(p):
    for f in list(lock):
        if lock[f] == p:
            del lock[f]
            print(f"{p} released {f}")


# execution
request("P1", "File_A")
request("P2", "File_B")
request("P1", "File_B")
request("P2", "File_A")