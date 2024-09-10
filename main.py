class Stack:
    def __init__(self):
        self.__stack = []
        self.__amount = 10

    def __str__(self):
        return f'this is stack with max amount = {self.__amount}'

    def is_stack_empty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False

    def is_stack_full(self):
        if len(self.__stack) == self.__amount:
            return True
        else:
            return False

    def add(self, item: str):
        if len(self.__stack) == self.__amount:
            raise Exception('stack is full')
        if type(item) is not str:
            raise Exception('item must be str')
        self.__stack.append(item)

    def remove(self):
        if len(self.__stack) == 0:
            raise Exception('stack is empty')
        self.__stack.pop(len(self.__stack) - 1)

    def __len__(self):
        return len(self.__stack)

    def clean(self):
        self.__stack = []

    def get_last_item(self):
        return self.__stack[len(self.__stack) - 1]


def menu():
    stack = Stack()
    while True:
        move = int(input('1 - add item to stack\n'
                         '2 - remove last item\n'
                         '3 - get length \n'
                         '4 - get last item \n'
                         '5 - check if stack is full \n'
                         '6 - check if stack is empty \n'
                         '7 - clean stack \n'))
        if move == 1:
            item = input('write item')
            stack.add(item)
        elif move == 2:
            stack.remove()
        elif move == 3:
            print(len(stack))
        elif move == 4:
            print(stack.get_last_item())
        elif move == 5:
            print(stack.is_stack_full())
        elif move == 6:
            print(stack.is_stack_empty())
        elif move == 7:
            stack.clean()


if __name__ == '__main__':
    menu()
