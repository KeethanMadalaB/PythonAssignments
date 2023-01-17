num1 = 131
num2 = str(num1)
num2 = int(num2[::-1])
if num1 == num2: print("Palindrome")
else: print("Not Palindrome")