import unittest
from linkedlist import LinkedList
from decorators import runtime_decorator, bold_decorator, italic_decorator, underline_decorator

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

    def test_length(self):
        self.assertEqual(len(self.linked_list), 3)

    def test_getitem(self):
        self.assertEqual(self.linked_list[1], 2)


class TestDecorators(unittest.TestCase):
    def test_runtime_decorator(self):
        @runtime_decorator
        def test_function():
            return "Test"
        
        self.assertEqual(test_function(), "Test")

    def test_bold_decorator(self):
        @bold_decorator
        def test_function():
            return "Test"
        
        self.assertEqual(test_function(), "<b>Test</b>")


if __name__ == "__main__":
    unittest.main()
