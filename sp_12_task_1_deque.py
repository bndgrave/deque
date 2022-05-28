class Deque:
    def __init__(self):
        self.items = []

    def push_front(self, item):
        self.items.insert(0, item)

    def push_back(self, item):
        self.items.append(item)

    def pop_front(self):
        try:
            print(self.items.pop())
        except IndexError:
            print('Удаление невозможно, дек пуст!')

    def pop_back(self):
        try:
            print(self.items.pop())
        except IndexError:
            print('Удаление невозможно, дек пуст!')

# def main(input_data):
#     pass

if __name__ == '__main__':
    d = Deque()
    print(d.items)
    [d.push_front(elem) for elem in range(2)]
    [d.push_back(elem) for elem in range(2)]
    print(d.items)
    [d.pop_back() for ind in range(len(d.items)+1)]
    print(d.items)