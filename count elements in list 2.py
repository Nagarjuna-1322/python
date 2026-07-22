 



 # Count Occurrences of an Element in a List

numbers = [1, 2, 3, 3, 4, 3]
element = 3
count = 0

for num in numbers:
    if num == element:
        count += 1

print("The element", element, "appears", count, "times.")
