mini = 2
maxi = 999999
power = 5
while mini <= maxi:
	
	temp = mini
	res = 0
	while(temp > 0):
		 res = res + pow(temp % 10, power)
		 if res > mini:
			break
		 temp = temp/10
	if res == mini:
		print(res)
	mini = mini + 1
