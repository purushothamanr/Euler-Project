n = 100
first = 1
last = 100
sum_of_100 = (n *( first + last))/2
square_of_sum = sum_of_100*sum_of_100

sum_of_square = temp =  first*first + last*last
difference_gap = (n-2) * 2

while (difference_gap >= 4):
	temp  = temp - difference_gap
	sum_of_square = sum_of_square + temp
	difference_gap = difference_gap - 4

print(sum_of_square, square_of_sum)
print(square_of_sum-sum_of_square)
