import operator

def sort_by_count(dictionary, assending=True):
  """Take a dictionary and return sorted tuples by value
  
  Example:
  >>> data = {'red': 3,
  ...         'blue': 20, 
  ...         'orange': 1}
  >>> 
  >>> sort_by_count(data)
  [('orange', 1), ('red', 3), ('blue', 20)]
  """

  # To make certain this is used correctly
  assert isinstance(dictionary, dict)

  return sorted(dictionary.iteritems(),
                key=operator.itemgetter(1),
                reverse=not assending)

y = {}
x = open('war_and_peace.txt', 'r')
for thing in x.readlines():
	if y.has_key(thing):
		y[thing] = y[thing] + 1
	else:
		y[thing] = 1
print sort_by_count(y)
