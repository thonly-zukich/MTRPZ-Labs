import unittest
from dual_array_list import DualArrayList

class DualArrayListTestSuite(unittest.TestCase):
    """Набір тестів для DualArrayList"""

    def setUp(self):
        """Створення нового списку перед кожним тестом"""
        self.custom_list = DualArrayList()

    def test_append(self):
        """Тест додавання елементів у список"""
        self.custom_list.append("A")
        self.custom_list.append("B")
        self.assertEqual(self.custom_list.length(), 2)
        self.assertEqual(self.custom_list.get(1), "B")

    def test_insert(self):
        """Тест вставки елементу за індексом"""
        self.custom_list.append("A")
        self.custom_list.append("C")
        self.custom_list.insert("B", 1)
        self.assertEqual(self.custom_list.get(1), "B")

    def test_delete(self):
        """Тест видалення елементу за індексом"""
        self.custom_list.append("A")
        self.custom_list.append("B")
        self.assertEqual(self.custom_list.delete(0), "A")
        self.assertEqual(self.custom_list.length(), 1)

    def test_deleteAll(self):
        """Тест видалення усіх однакових елементів"""
        self.custom_list.append("A")
        self.custom_list.append("B")
        self.custom_list.append("A")
        self.custom_list.deleteAll("A")
        self.assertEqual(self.custom_list.length(), 1)

    def test_get(self):
        """Тест отримання елементу за індексом"""
        self.custom_list.append("A")
        self.assertEqual(self.custom_list.get(0), "A")

    def test_clone(self):
        """Тест копіювання списку"""
        self.custom_list.append("A")
        cloned = self.custom_list.clone()
        self.assertEqual(cloned.length(), 1)
        self.assertEqual(cloned.get(0), "A")

    def test_reverse(self):
        """Тест реверсу списку"""
        self.custom_list.append("A")
        self.custom_list.append("B")
        self.custom_list.reverse()
        self.assertEqual(self.custom_list.get(0), "B")

    def test_findFirst(self):
        """Тест знаходження першого входження"""
        self.custom_list.append("A")
        self.custom_list.append("B")
        self.custom_list.append("A")
        self.assertEqual(self.custom_list.findFirst("A"), 0)

    def test_findLast(self):
        """Тест знаходження останнього входження"""
        self.custom_list.append("A")
        self.custom_list.append("B")
        self.custom_list.append("A")
        self.assertEqual(self.custom_list.findLast("A"), 2)

    def test_clear(self):
        """Тест очищення списку"""
        self.custom_list.append("A")
        self.custom_list.clear()
        self.assertEqual(self.custom_list.length(), 0)

    def test_extend(self):
        """Тест розширення списку іншим списком"""
        self.custom_list.append("A")
        additional_list = DualArrayList()
        additional_list.append("B")
        self.custom_list.extend(additional_list)
        self.assertEqual(self.custom_list.length(), 2)
        self.assertEqual(self.custom_list.get(1), "B")

if __name__ == '__main__':
    unittest.main()
