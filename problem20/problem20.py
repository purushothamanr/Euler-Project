
def factorial(x):
	if x == 1:
		return x 

	result = x*factorial(x-1)
	return result

a = factorial(100)
print(a)

result = 0

while a > 1:
	result = result + a % 10
	a = a / 10

print(result)

