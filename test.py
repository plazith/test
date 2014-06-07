import unittest
from code import Stack

class StackExamples(unittest.TestCase):
	def setUp(self):
		self.s = Stack()

	def test_existance(self):
		self.assertTrue(isinstance(self.s, Stack))

	def test_empty(self):
		self.assertTrue(self.s.is_empty())

	def test_push(self):
		self.s.push(7)
		value = self.s.pop()
		self.assertEqual(value, 7)

	def test_pop_empty(self):
		self.assertRaises(ValueError, self.s.pop)

	def test_size_one_element(self):
		self.s.push('an element')
		self.assertEqual(self.s.get_size(), 1)

	def test_size_two_elements(self):
		self.s.push(1.343)
		self.s.push(-343)
		self.assertEqual(self.s.get_size(), 2)

	def test_size_one_element_popped(self):
		self.s.push('apple')
		self.s.pop()
		self.assertTrue(self.s.is_empty())

	def test_push_two_items(self):
		self.s.push('anything')
		self.s.push(10)
		value = self.s.pop()
		self.assertEqual(value, 10)
	
	def test_peek_on_empty(self):
		self.assertEqual(self.s.peek(), None)

	def test_peek_one_item(self):
		self.s.push('something')
		self.assertEqual(self.s.peek(), 'something')

if __name__ == '__main__':
	unittest.main()
