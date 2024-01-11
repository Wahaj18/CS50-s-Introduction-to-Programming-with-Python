class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("No Capacity Left")
        else:
            self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies")
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity can't be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Jar is full of cookies already")
        else:
            self._size = size

def main():
    jar = Jar()
    print(jar)
    jar.deposit(10)
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.withdraw(5)
    print(jar)

if __name__ == "__main__":
    main()
