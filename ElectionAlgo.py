class Election:
    def __init__(self):
        self.processes = [1,2,3,4,5,6,7,8,9,10]
        self.active = {p: True for p in self.processes}

    def start(self):
        self.election(3)   # any process can start

    def election(self, p):
        print(f"\nProcess {p} starts election")

        higher = [i for i in self.processes if i > p and self.active[i]]

        if not higher:
            print(f"\nProcess {p} becomes COORDINATOR")
            self.coordinator(p)
        else:
            print(f"Process {p} sends ELECTION to {higher}")

            for h in higher:
                print(f"Process {h} replies OK")

            # highest active process continues election
            self.election(max(higher))

    def coordinator(self, c):
        print("\nCoordinator Announcement:")
        for p in self.processes:
            if p != c and self.active[p]:
                print(f"Process {c} informs Process {p}")


e = Election()
e.start()