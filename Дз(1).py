class Counter:
    def start_from(self, n=0):
        self.n = n
    def increment(self):
        self.n += 1

    def display(self):
        print(f"Текущее значение счетчика = {self.n}")

    def reset(self):
        self.n = 0

c1 = Counter()
c1.start_from(3)
c1.increment()
c1.display()
c1.reset()
c1.display()