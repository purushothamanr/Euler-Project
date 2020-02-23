import operator
i = 2
dict_count = {}

dict_count[1] = 1
 
while i <= 26:
	temp = i
	count = 0	
	while temp >= 1:
		if temp in dict_count:
			count = count + dict_count[temp]
			break
		if temp % 2 == 0:
			temp = temp/2
			count = count + 1
		else:
			temp = (3 * temp) + 1
			count = count + 1
	dict_count[i] = count
	i = i + 1
print(max(dict_count.iteritems(), key=operator.itemgetter(1))[0])
			
