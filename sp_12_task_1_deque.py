# Номер посылки - 68726758

class DequeUpdateError(BaseException):
    """Класс исключений для обработки """
    def __init__(self, *args, **kwargs):
        if args:
            self.message = args[0]
        else:
            self.message = 'error'

    def __str__(self):
        return self.message


class Deque:
    def __init__(self, deque_length):
        self.__items = [None] * deque_length
        self.__max_items = deque_length
        self.__first = 0
        self.__last = 0
        self.__size = 0
    
    def __is_empty(self):
        return self.__size == 0

    def __is_full(self):
        return self.__size == self.__max_items

    def __move_pointer_left(self, pointer):
        attr = getattr(self, pointer)
        return (attr - 1) % self.__max_items
    
    def __move_pointer_right(self, pointer):
        attr = getattr(self, pointer)
        return (attr + 1) % self.__max_items

    def push_front(self, item):
        if self.__is_full():
            raise DequeUpdateError()
        self.__items[self.__first] = item
        self.__first = self.__move_pointer_left('_Deque__first')
        self.__size += 1
            
    def push_back(self, item):
        if self.__is_full():
            raise DequeUpdateError()
        self.__last = self.__move_pointer_right('_Deque__last')
        self.__items[self.__last] = item
        self.__size += 1

    def pop_front(self):
        if self.__is_empty():
            raise DequeUpdateError()
        self.__first = self.__move_pointer_right('_Deque__first')
        item = self.__items[self.__first]
        self.__items[self.__first] = None
        self.__size -= 1
        return item

    def pop_back(self):
        if self.__is_empty():
            raise DequeUpdateError()
        item = self.__items[self.__last]
        self.__items[self.__last] = None
        self.__last = self.__move_pointer_left('_Deque__last')
        self.__size -= 1
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
    deque = Deque(input_data['deque_length'])
    for command in input_data['commands']:
        method = getattr(deque, command[0])
        try:
            result = (
                method(int(command[1])) if len(command) == 2 else method()
            )
            if result is not None:
                print(result)
        except DequeUpdateError as error:
            print(error)
