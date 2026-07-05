 
 

#Instead of just converting the number to a string and using slicing, the speaker demonstrates the algorithmic logic:
#Modulo Operator (% 10): Used to extract the last digit of the number (e.g., in 703, it pulls out the 3).
#String Concatenation: The extracted digit is converted to a string and added to a variable storing the reversed result.
#Integer Division (// 10): Used to update the number by removing the last digit (e.g., changing 703 to 70).
#Looping: A while loop is used to repeat this process as long as the number is greater than zero.


num = int(input("enter the number"))

reversed_number=""
while(num>0):
    
    
# digit = num%10
#reversed_number +=str(digit)


 num = num//10

print(reversed_number)