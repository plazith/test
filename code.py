"""My TDD Stack Module"""

class Stack(object):
	"""My TDD Stack Class"""
	def __init__(self):
		self.stack_contents = []

	def get_size(self):
		return len(self.stack_contents)

	def is_empty(self):
		return len(self.stack_contents) == 0

	def peek(self):
		if self.stack_contents:
			return self.stack_contents[-1]
		else:
			return None

	def pop(self):
		if self.stack_contents:
			value = self.stack_contents[-1]
			self.stack_contents = self.stack_contents[:-1]
			return value
		else:
			raise ValueError

	def push(self, item):
		self.stack_contents.append(item)
