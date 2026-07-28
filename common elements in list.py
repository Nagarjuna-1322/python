

# find common elements in two lists

# Input lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

# Find common elements
common = []

for item in list1:
    if item in list2:
        common.append(item)

# Display result
print("Common Elements:", common)