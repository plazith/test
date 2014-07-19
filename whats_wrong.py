import csv

with open('whats_wrong.csv', 'rb') as csvfile:
	wrongreader = csv.reader(csvfile)
	for row in wrongreader:
		first_name = row[0]
		last_name = row[1]
		address = row[2]
		description = row[3]
		if first_name == "firstname": continue
		print "First Name: ", first_name
		print "Last Name: ", last_name
		print "Address: ", address
		print "Description: ", description
