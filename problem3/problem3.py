number=600851475143

n = 2
max = 1

while (n <= number):
	if number == 1:
	   break
	if number % n == 0:
	    print(n)
	    number = number/n
	    max = n
	n = n + 1

print("max is" ,max)
