


#Find the Missing Number in a List
#Problem: Given a list of numbers from 1 to n, with one number missing, find the missing number.
#Example:Input: [1, 2, 4, 5], n = 5Output: 3



numbers = [1, 2, 4, 5]
n = 5

for i in range(1, n + 1):
    if i not in numbers:
        print("Missing Number:", i)
        break