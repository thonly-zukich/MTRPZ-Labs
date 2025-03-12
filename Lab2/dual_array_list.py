class DualArrayList:
    def __init__(self):
        """Ініціалізація двобічного списку на масивах"""
        self.elements = []

    def length(self) -> int:
        """Повертає кількість елементів у списку"""
        return len(self.elements)

    def append(self, element: str) -> None:
        """Додає елемент у кінець списку"""
        self.elements.append(element)

    def insert(self, element: str, index: int) -> None:
        """Вставляє елемент на задану позицію"""
        if index < 0 or index > len(self.elements):
            raise IndexError("Index out of range")
        self.elements.insert(index, element)

    def delete(self, index: int) -> str:
        """Видаляє елемент за позицією та повертає його"""
        if index < 0 or index >= len(self.elements):
            raise IndexError("Index out of range")
        return self.elements.pop(index)

    def deleteAll(self, element: str) -> None:
        """Видаляє всі елементи зі списку, що відповідають значенню"""
        self.elements = [e for e in self.elements if e != element]

    def get(self, index: int) -> str:
        """Отримує елемент за індексом"""
        if index < 0 or index >= len(self.elements):
            raise IndexError("Index out of range")
        return self.elements[index]

    def clone(self):
        """Створює копію списку"""
        cloned_list = DualArrayList()
        cloned_list.elements = self.elements[:]
        return cloned_list

    def reverse(self) -> None:
        """Реверсує порядок елементів у списку"""
        self.elements.reverse()

    def findFirst(self, element: str) -> int:
        """Повертає індекс першого входження елемента або -1, якщо його немає"""
        return self.elements.index(element) if element in self.elements else -1

    def findLast(self, element: str) -> int:
        """Повертає індекс останнього входження елемента або -1, якщо його немає"""
        return len(self.elements) - 1 - self.elements[::-1].index(element) if element in self.elements else -1

    def clear(self) -> None:
        """Очищає список"""
        self.elements.clear()

    def extend(self, other_list) -> None:
        """Додає всі елементи з іншого списку"""
        if not isinstance(other_list, DualArrayList):
            raise TypeError("Argument must be an instance of DualArrayList")
        self.elements.extend(other_list.elements)
