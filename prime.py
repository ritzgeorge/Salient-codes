for a in range(1,101):
	if a%2==0:
		if a==2:
			print(a)
		continue
	elif a%3==0 or a%5==0 or a%7==0:
		if a==3 or a==7 or a==5:
			print(a)
	else:
		print(a)



