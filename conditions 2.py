#Given an integer, , perform the following conditional actions:

#f  is odd, print Weird
#f  is even and in the inclusive range of  2 to 5 , print Not Weird 
#f  is even and in the inclusive range of 6 to 20 , print Weird 
#f  is even and greater than , print Not Weird


n = int(input("enter the number"))

if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")