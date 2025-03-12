class NodeItem:
    """Клас вузла двобічно зв'язаного списку"""
    def __init__(self, symbol: str):
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Node data must be a single character.")
        self.symbol = symbol
        self.next_node = None  # Посилання на наступний вузол
        self.prev_node = None  # Посилання на попередній вузол

class DualLinkedList:
    """Клас двобічно зв'язаного списку"""
    def __init__(self):
        self.start = None  # Початковий елемент списку
        self.end = None  # Кінцевий елемент списку
        self.count = 0     # Кількість елементів у списку

    def size(self) -> int:
        """Повертає кількість елементів у списку"""
        return self.count

    def add(self, character: str):
        """Додає елемент у кінець списку"""
        new_node = NodeItem(character)
        if not self.start:
            self.start = self.end = new_node
        else:
            self.end.next_node = new_node
            new_node.prev_node = self.end
            self.end = new_node
        self.count += 1

    def insert(self, character: str, index: int):
        """Вставляє елемент у довільну позицію"""
        if index < 0 or index > self.count:
            raise IndexError("Index out of range")
        new_node = NodeItem(character)
        if index == 0:
            new_node.next_node = self.start
            if self.start:
                self.start.prev_node = new_node
            self.start = new_node
            if self.count == 0:
                self.end = new_node
        elif index == self.count:
            self.add(character)
        else:
            current = self.start
            for _ in range(index):
                current = current.next_node
            new_node.prev_node = current.prev_node
            new_node.next_node = current
            if current.prev_node:
                current.prev_node.next_node = new_node
            current.prev_node = new_node
        self.count += 1

    def remove(self, index: int) -> str:
        """Видаляє елемент за індексом"""
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")
        if index == 0:
            removed = self.start
            self.start = self.start.next_node
            if self.start:
                self.start.prev_node = None
        elif index == self.count - 1:
            removed = self.end
            self.end = self.end.prev_node
            self.end.next_node = None
        else:
            current = self.start
            for _ in range(index):
                current = current.next_node
            removed = current
            current.prev_node.next_node = current.next_node
            if current.next_node:
                current.next_node.prev_node = current.prev_node
        self.count -= 1
        return removed.symbol

    def remove_all(self, character: str):
        """Видаляє всі елементи зі значенням `character`"""
        current = self.start
        while current:
            if current.symbol == character:
                if current == self.start:
                    self.start = current.next_node
                    if self.start:
                        self.start.prev_node = None
                elif current == self.end:
                    self.end = current.prev_node
                    if self.end:
                        self.end.next_node = None
                else:
                    current.prev_node.next_node = current.next_node
                    current.next_node.prev_node = current.prev_node
                self.count -= 1
            current = current.next_node

    def get(self, index: int) -> str:
        """Повертає елемент за індексом"""
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")
        current = self.start
        for _ in range(index):
            current = current.next_node
        return current.symbol

    def duplicate(self):
        """Клонує список"""
        cloned_list = DualLinkedList()
        current = self.start
        while current:
            cloned_list.add(current.symbol)
            current = current.next_node
        return cloned_list

    def reverse(self):
        """Реверсує порядок елементів у списку"""
        current = self.start
        while current:
            current.next_node, current.prev_node = current.prev_node, current.next_node
            current = current.prev_node
        self.start, self.end = self.end, self.start

    def find_first(self, character: str) -> int:
        """Знаходить перше входження елемента"""
        current = self.start
        index = 0
        while current:
            if current.symbol == character:
                return index
            current = current.next_node
            index += 1
        return -1

    def find_last(self, character: str) -> int:
        """Знаходить останнє входження елемента"""
        current = self.end
        index = self.count - 1
        while current:
            if current.symbol == character:
                return index
            current = current.prev_node
            index -= 1
        return -1

    def clear(self):
        """Очищає список"""
        self.start = self.end = None
        self.count = 0
    

    def extend(self, other_list):
        """Додає всі елементи з іншого списку"""
        current = other_list.start
        while current:
            self.add(current.symbol)  
            current = current.next_node

    
