
num = int(input("Enter num : "))

def factorial(num):

    i=1
    fact=1 
    while i<=num:
        fact = fact*i
        i= i+1
    return fact

print(f"Factorial of number :  {factorial(num)}")
