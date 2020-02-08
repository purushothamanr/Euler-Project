final_destination = 2000000
a = []
i=1
while i <= final_destination:
	a.append(i)
	i = i + 1

loop_start = loop = 1
loop_jump = 2
summ = 0
while(loop < len(a)):
	if loop == loop_start:
		if a[loop] == 0:
			loop_jump = loop_jump + 1
                	loop_start = loop_start + 1
                	loop = loop_start
			continue
		else:
			summ = summ + a[loop]

	if loop == len(a)-1 or loop+loop_jump > len(a)-1:
		loop_jump = loop_jump + 1
		loop_start = loop_start + 1
		loop = loop_start
	else:
		loop = loop + loop_jump
        	a[loop] = 0

#i = 1
#sum = 0
#while (i < len(a)):
#	sum = sum + a[i]
#	i = i + 1

print(summ)	

