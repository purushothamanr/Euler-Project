array_size = 20
base_routes = 2
d_2 = [[0 for x in range(array_size)] for y in range(array_size)] 

i = 0
j = 0
while i < array_size:
	j = 0
	while j < array_size:
		if i == 0:
			d_2[i][j] = base_routes + j
		else:
			if j == 0:
				d_2[i][j] = base_routes + i
			else:
				d_2[i][j] = d_2[i][j-1] + d_2[i-1][j]
		j = j + 1
	i = i + 1

print(d_2) 
