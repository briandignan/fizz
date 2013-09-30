print 'hello'

for i in range( 1, 101):
	if i % 15 == 0:
		print 'fizzybuzzy'
	elif i % 5 == 0:
		print 'buzzy'
	elif i % 3 == 0:
		print 'fizzy'
	else: 
		print i

