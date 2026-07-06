

def fizzBuzz(n):
    # Loop through integers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # 1. Check if divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # 2. Check if divisible by 3 only
        elif i % 3 == 0:
            print ("Fizz")
        # 3. Check if divisible by 5 only
        elif i % 5 == 0:
            print ("Buzz")
        # 4. If none of the above, print the number itself
        else:
            print (i)