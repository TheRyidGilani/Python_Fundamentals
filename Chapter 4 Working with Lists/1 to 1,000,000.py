numbers= []

for values in range(1,1000001):
    numbers.append(values)
    print(values)

print("\nThe smallest number is: " + str(min(numbers)))
print("The biggest number is: " + str(max(numbers)))

print("The sum of all the numbers is: " + str(sum(numbers)))

