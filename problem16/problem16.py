import json
i = 0

dict_loop_up = {}

while i <= 1000:
	a = pow(2, i)
        result = 0

	while a > 0:
		result = result + a % 10
		a = a / 10
	print(result)

	if result not in dict_loop_up:
		dict_loop_up[result] = 1
	else:
		dict_loop_up[result] = dict_loop_up[result] + 1
		
	i = i + 1

print(len(dict_loop_up))
print json.dumps(dict_loop_up, indent=1)
