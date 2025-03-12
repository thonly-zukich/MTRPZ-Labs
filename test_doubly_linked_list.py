import unittest
from doubly_linked_list import DualLinkedList

class DualLinkedListTestSuite(unittest.TestCase):
    """Тести для класу DualLinkedList"""

    def setUp(self):
        """Ініціалізація нового списку перед кожним тестом"""
        self.custom_list = DualLinkedList()
        for ch in ["A", "B", "C"]:
            self.custom_list.add(ch)

    def test_length_verification(self):
        """Перевіряємо коректність визначення розміру списку"""
        self.assertEqual(self.custom_list.size(), 3)

    def test_adding_elements(self):
        """Тестуємо додавання нового вузла у кінець"""
        self.custom_list.add("Z")
        self.assertEqual(self.custom_list.size(), 4)
        self.assertEqual(self.custom_list.get(3), "Z")

    def test_insert_middle(self):
        """Перевіряємо вставку елемента в середину списку"""
        self.custom_list.insert("M", 1)
        self.assertEqual(self.custom_list.get(1), "M")
        self.assertEqual(self.custom_list.size(), 4)

    def test_delete_by_index(self):
        """Тестуємо видалення елемента за індексом"""
        removed_value = self.custom_list.remove(1)
        self.assertEqual(removed_value, "B")
        self.assertEqual(self.custom_list.size(), 2)

    def test_mass_deletion(self):
        """Перевіряємо видалення всіх елементів зі значенням"""
        self.custom_list.add("B")
        self.custom_list.remove_all("B")
        self.assertEqual(self.custom_list.size(), 2)
        self.assertEqual(self.custom_list.find_first("B"), -1)

    def test_element_retrieval(self):
        """Переконуємося, що метод get() працює як треба"""
        self.assertEqual(self.custom_list.get(0), "A")
        self.assertEqual(self.custom_list.get(2), "C")

    def test_list_reversal(self):
        """Реверсуємо список і перевіряємо коректність змін"""
        self.custom_list.reverse()
        self.assertEqual(self.custom_list.get(0), "C")
        self.assertEqual(self.custom_list.get(2), "A")

    def test_duplicate_function(self):
        """Тестуємо клонування списку"""
        clone = self.custom_list.duplicate()
        self.assertEqual(clone.size(), self.custom_list.size())
        self.assertEqual(clone.get(0), "A")
        self.assertEqual(clone.get(1), "B")

    def test_locate_first_occurrence(self):
        """Шукаємо перше входження елемента"""
        self.custom_list.add("B")
        self.assertEqual(self.custom_list.find_first("B"), 1)

    def test_locate_last_occurrence(self):
        """Шукаємо останнє входження елемента"""
        self.custom_list.add("B")
        self.assertEqual(self.custom_list.find_last("B"), 3)

    def test_wipe_list(self):
        """Очищаємо список і перевіряємо, що він пустий"""
        self.custom_list.clear()
        self.assertEqual(self.custom_list.size(), 0)

    def test_expanding_list(self):
        """Додаємо вміст іншого списку"""
        additional_list = DualLinkedList()
        for ch in ["X", "Y"]:
            additional_list.add(ch)

        self.custom_list.extend(additional_list)
        self.assertEqual(self.custom_list.size(), 5)
        self.assertEqual(self.custom_list.get(3), "X")
        self.assertEqual(self.custom_list.get(4), "Y")

if __name__ == "__main__":
    unittest.main()
