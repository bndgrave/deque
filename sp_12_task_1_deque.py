class Deque:
    def __init__(self, deque_length):
        self.items = [None] * deque_length
        self.max_items = deque_length
        self.first = 0
        self.last = 0
        self.size = 0
    
    def is_empty(self):
        return self.size == 0

    def push_front(self, item):
        if self.size != self.max_items:
            self.items[self.first] = item
            self.first = (self.first - 1) % self.max_items
            self.size += 1
            
    def push_back(self, item):
        if self.size != self.max_items:
            self.last = (self.last + 1) % self.max_items
            self.items[self.last] = item
            self.size += 1

    def pop_front(self):
        if self.is_empty():
            return None
        self.first = (self.first + 1) % self.max_items
        item = self.items[self.first]
        self.items[self.first] = None
        self.size -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            return None
        item = self.items[self.last]
        self.items[self.last] = None
        self.last = (self.last - 1) % self.max_items
        self.size -= 1
        return item

if __name__ == '__main__':
    deque_length = int(input())
    # commands_number = int(input())
    d = Deque(deque_length)
    print(d.items)
    # for number in range(commands_number):
    #     command = input().split(' ')
    #     method = getattr(d, command[0])
    #     method(int(command[1])) if len(command) == 2 else method()
    # print(d.items)
    # d.pop_back(None)
    [d.push_front(elem) for elem in range(2)]
    [d.push_back(elem) for elem in range(3)]
    print(d.items)
    [d.pop_back() for ind in range(2)]
    print(d.items)
    [d.pop_front() for ind in range(2)]
    print(d.items)
    d.push_front(10)
    d.push_back(11)
    print(d.items)
    # method = getattr(d, 'pop_back')
    # method()
    # print(d.items)