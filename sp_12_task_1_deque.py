# Номер посылки - 68673533

class Deque:
    def __init__(self, deque_length):
        self.items = [None] * deque_length
        self.max_items = deque_length
        self.first = 0
        self.last = 0
        self.size = 0
    
    def is_empty(self):
        if self.size == 0:
            print('error')
        return self.size == 0

    def is_full(self):
        if self.size == self.max_items:
            print('error')
        return self.size == self.max_items

    def push_front(self, item):
        if not self.is_full():
            self.items[self.first] = item
            self.first = (self.first - 1) % self.max_items
            self.size += 1
            
    def push_back(self, item):
        if not self.is_full():
            self.last = (self.last + 1) % self.max_items
            self.items[self.last] = item
            self.size += 1

    def pop_front(self):
        if not self.is_empty():
            self.first = (self.first + 1) % self.max_items
            item = self.items[self.first]
            print(item)
            self.items[self.first] = None
            self.size -= 1
            return item

    def pop_back(self):
        if not self.is_empty():
            item = self.items[self.last]
            print(item)
            self.items[self.last] = None
            self.last = (self.last - 1) % self.max_items
            self.size -= 1
            return item


def read_input_data():
    input_data = dict()
    commands_num = int(input())
    input_data['deque_length'] = int(input())
    input_data['commands'] = []
    for number in range(commands_num):
        command = input().split(' ')
        input_data['commands'].append(command)
    return input_data

if __name__ == '__main__':
    input_data = read_input_data()
    d = Deque(input_data['deque_length'])
    for command in input_data['commands']:
        method = getattr(d, command[0])
        method(int(command[1])) if len(command) == 2 else method()
