from math import sqrt, ceil

found = 0
n1 = 1
n2 = 0
n3 = 0

while found < 3:
	n2 = int(ceil(n1*n1/3.0))
	n3 = int(ceil(n1*n1/4.0))
	n2 = int(ceil(sqrt(n2)))
	n3 = int(ceil(sqrt(n3)))
	
	tri = (n1*n1+n1)/2
	pent = (3*n2*n2-n2)/2
	hexa = (4*n3*n3-2*n3)/2
	print((n1*n1+n1)/2, (3*n2*n2-n2)/2, (4*n3*n3-2*n3)/2)
	
	if tri == pent == hexa:
		found = found + 1
		print(tri)
	n1 = n1 + 1
