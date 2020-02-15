#Question 4
f = open('housing.data', 'r')
if path.exists('housing.data'):
    print('I have a file to process')
else:
    print('Boo, no file for me')

#Question 5 - Read file
f = open('housing.data', 'r')

#Question 6 - Print line by line
for line in f:
    print(line)

#Question 7 - read in list
f = open('housing.data', 'r')
list(f)