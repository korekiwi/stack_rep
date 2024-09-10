from typing import Union


class Box:
    def __init__(self, value, next_box: Union['Box', None] = None,
                 prev_box: Union['Box', None] = None):
        self.__value = value
        self.__next_box = next_box
        self.__prev_box = prev_box

    def __str__(self):
        return f'{self.__value}, {self.__next_box}'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.__value = v

    @property
    def link_next_box(self):
        return self.__next_box

    @property
    def link_prev_box(self):
        return self.__prev_box

    @link_next_box.setter
    def link_next_box(self, b: Union['Box', None]):
        if isinstance(b, Box):
            b.__prev_box = self
            self.__next_box = b
        elif b is None:
            self.__next_box = b
        else:
            raise Exception()

    @link_prev_box.setter
    def link_prev_box(self, b):
        if isinstance(b, Box) or b is None:
            self.__prev_box = b
        else:
            raise Exception()


class LinkList:
    def __init__(self):
        self.__len = 0
        self.__head: Union[Box, None] = None
        self.__tail: Union[Box, None] = None

    def __len__(self):
        return self.__len

    def __str__(self):
        if self.__head is not None:
            return str(self.__head)
        return "[]"

    def add(self, value):
        new_box = Box(value=value)
        self.__len += 1
        if self.__head is None:
            self.__head = new_box
            self.__tail = new_box
            return

        temp_box = self.__tail
        temp_box.link_next_box = new_box
        self.__tail = new_box

    def __search(self, value) -> Union[Box, None]:
        temp_box = self.__head
        while temp_box is not None and temp_box.value != value:
            temp_box = temp_box.link_next_box
        return temp_box

    def remove(self, value):
        if self.__head is not None:
            if self.__head.value == value:
                if self.__head.value == self.__tail.value:
                    self.__head = None
                    self.__tail = None
                    return
                next_box = self.__head.link_next_box
                next_box.link_prev_box = None
                self.__head = next_box
                return
            sought_box = self.__search(value)
            if sought_box is not None:
                prev_box = sought_box.link_prev_box
                next_box = sought_box.link_next_box
                prev_box.link_next_box = next_box


link_list = LinkList()
link_list.add(1)
link_list.add(3)
link_list.add(2)
link_list.add(5)
link_list.remove(1)
print(link_list)
