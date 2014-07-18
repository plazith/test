f = open('whats_wrong.csv', 'r')
lines = f.readlines()
for line in lines:
    line = line.rstrip('\n')
    line = line.split(',')
    first_name = line[0]
    last_name = line[1]
    address = line[2]
    description = line[3]
    if first_name == "firstname": continue
    print "First Name: ", first_name
    print "Last Name: ", last_name
    print "Address: ", address
    print "Description: ", description
f.close


