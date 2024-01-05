n = int(input("Enter a number: "))

# Classify the number
if n < 0:
    print("The number is negative.")
elif n == 0:
    print("The number is zero.")
elif n > 0:
    print("The number is positive.")
else:
    print("Please enter numbers.")
