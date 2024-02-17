values = [-10000, 100, 1000, 5, 500, -500, 30]
#find the max and min
min = values[0]
max = values[0]

for value in values:
   if value > max:
       max = value

   if value < min:
       min = value

print(max)
print(min)