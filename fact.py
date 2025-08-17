fact=int(input("Enter a number: "))
def factorial (fact):

    if fact < 2:
        return 1
    else:
        return fact * factorial(fact- 1)
result = factorial(fact)
print(f"The factorial of {fact} is: {result}")    
