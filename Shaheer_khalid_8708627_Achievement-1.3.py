#Here I start by importing math functions in order to get the square root function for this program
import math
#Here I take the user's Input and store it in the variable 'num'
print("Please enter an integer")
num = int(input())


#Now I use the built in python functions to get my results
#In this case I used oct()
print("Equivalent Octal value")
print(oct(num))

#Here I used hex()
print("Equivalent Hex value")
print(hex(num))

#After importing math functions I was able to use the math.sqrt() function to get the square root.
print("The Square Root of the given integer")
print(math.sqrt(num))