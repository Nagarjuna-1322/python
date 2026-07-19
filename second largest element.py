



# Input list
numbers = [10, 20, 4, 45, 99]

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest Element:", second_largest)