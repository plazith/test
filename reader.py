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


x = open('numbers.txt', 'r')
for thing in x.readlines():
	print thing
