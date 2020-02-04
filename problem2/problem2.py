prev = 0
curr = 2
sum = 2

while (prev + curr*4  < 4000000):
   temp = prev + curr*4
   sum = sum + temp
   prev = curr 
   curr = temp
   print(curr, prev)

print(sum)



