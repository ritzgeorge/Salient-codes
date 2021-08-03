def call(r,c):
	
	for row in range(r):
		if row%2==0:
			for col in range(c):
				
				if col%2==0:
					
					print('a',end='')
					
				else:
					
					print('|',end='')
				if col==c-1:
					print(' ')	
		else:
				for col in range(c):
					if col%2==0:
					
						print('z',end='')
					
					else:
					
						print('|',end='')
					if col==c-1:
						print(' ')		

call(10,10)
