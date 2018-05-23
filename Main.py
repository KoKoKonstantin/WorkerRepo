class Worker:
    def __init__(self, n):
        self.target = n

    def count_to_target(self):
        i = 0
        while i < self.target:
            print(i+1)
            i+=1


if __name__ == "__main__":
    w = Worker(5)
    w.count_to_target()