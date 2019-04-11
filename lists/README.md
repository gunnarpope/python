# How to find stuff in python lists
gunnarpope 4/10/19

		a = [1,2,3,4]
		
		# find the first occurance of x > 2
		print( next( x for x in a if x > 2))
		
		# find index of x = 2
		a.index(2)
		
		# find the first occurance of x > 2
		for x in a:
		    if x > 2:
		        print(x)
		        break;

		# Output 
			3
			3
