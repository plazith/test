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
for line in x.readlines():
	line = line.strip()
	for word in line.split(' '):
		word = word.lower()
		word = word.replace("'", "")
		if word == '':
			continue

		if y.has_key(word):
			y[word] = y[word] + 1
		else:
			y[word] = 1
thing = sort_by_count(y, False)
print thing[0:9]
